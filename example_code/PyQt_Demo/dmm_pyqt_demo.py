from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QPushButton)
from PyQt5.QtCore import *
from socket import *
import _thread
import time

g_serve_ip = '127.0.0.1'
g_serve_port = 3000
g_tcp_socket = socket(AF_INET, SOCK_STREAM)

g_recv_thread_loop = True
g_recv_get_data = False
g_recv_data_buf = b''


def recv_thread():
    global g_recv_get_data
    global g_recv_data_buf
    g_recv_get_data = False
    while g_recv_thread_loop:
        try:
            g_recv_data_buf = g_tcp_socket.recv(10000)
            g_recv_get_data = True
        except:
            print('close tcp socket.')


def set_up_tcp_client():
    # global recv_thread
    g_tcp_socket.connect((g_serve_ip, g_serve_port))
    try:
        _thread.start_new_thread(recv_thread, ())
    except:
        print("Error: can not start thread")


def scpi_query(delay_s, cmd_str):
    global g_recv_get_data
    global g_recv_data_buf
    g_recv_get_data = False
    count = 0
    g_tcp_socket.send(cmd_str.encode("gbk"))
    while True:
        if g_recv_get_data:
            return g_recv_get_data, g_recv_data_buf
        else:
            time.sleep(0.1)
            count += 1
            if count % 20 == 0:
                print(g_recv_get_data, count, delay_s)
            if count >= delay_s * 10:
                print("Error: ", count, delay_s)
                return g_recv_get_data, ''


def exit_all():
    global g_recv_thread_loop
    g_recv_thread_loop = False
    g_tcp_socket.close()


class GetValue(QtCore.QObject):
    flag_signal = pyqtSignal(str)
    data_signal = pyqtSignal(str)

    def __int__(self):
        super(GetValue, self).__int__()

    def runWork(self):
        while True:
            get_data, recv_data_buf = scpi_query(2, ':DMM:FUNCtion?\r\n')
            if get_data:
                recv_volt_or_curr = recv_data_buf.decode("gbk")
                self.flag_signal.emit(recv_volt_or_curr)
            get_data, recv_data_buf = scpi_query(2, ':DMM:MEAS?\r\n')
            if get_data:
                recv_buf = recv_data_buf.decode("gbk")
                self.data_signal.emit(recv_buf)
            QThread.sleep(1)


class MainWindow(QWidget):
    getValue = GetValue()
    thread = QtCore.QThread()
    volt_or_curr = ''

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setFixedSize(self.width(), self.height())

        set_up_tcp_client()

        self.value = QLabel()
        font = QtGui.QFont()
        font.setPointSize(24)
        self.value.setFont(font)
        self.value.setAlignment(Qt.AlignCenter)
        self.value.setText("Voltage: ")

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.value)
        self.setLayout(mainLayout)
        self.getValue.moveToThread(self.thread)
        self.getValue.data_signal.connect(self.updateValue)
        self.getValue.flag_signal.connect(self.updateFlag)
        self.thread.started.connect(self.getValue.runWork)
        self.thread.start()

    def updateFlag(self, flag):
        self.volt_or_curr = flag

    def updateValue(self, value):
        if self.volt_or_curr == 'mV' or self.volt_or_curr == 'V':
            self.value.setText("Voltage: " + value + " " + self.volt_or_curr)
        elif self.volt_or_curr == 'uA' or self.volt_or_curr == 'mA' or self.volt_or_curr == 'A':
            self.value.setText("Current: " + value + " " + self.volt_or_curr)
        else:
            self.value.setText("Not Support")

    def __del__(self):
        self.thread.quit()
        self.thread.deleteLater()
        exit_all()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setWindowTitle("DMM Python Demo")

    mainWindow.show()
    sys.exit(app.exec_())
