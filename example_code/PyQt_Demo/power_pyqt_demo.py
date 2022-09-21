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


class GetVoltage(QtCore.QObject):
    data_signal = pyqtSignal(str)

    def __int__(self):
        super(GetVoltage, self).__int__()

    def runWork(self):
        while True:
            get_data, recv_data_buf = scpi_query(10, ':MEASUrement:VOLTage?\r\n')
            if get_data:
                recv_buf = recv_data_buf.decode("gbk")
                self.data_signal.emit(recv_buf)
            QThread.sleep(1)


class MainWindow(QWidget):
    getVoltage = GetVoltage()
    thread = QtCore.QThread()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setFixedSize(self.width(), self.height())

        set_up_tcp_client()

        self.voltage = QLabel()
        font = QtGui.QFont()
        font.setPointSize(24)
        self.voltage.setFont(font)
        self.voltage.setAlignment(Qt.AlignCenter)
        self.voltage.setText("Voltage: ")

        self.button1 = QPushButton("1V")
        self.button1.clicked.connect(self.button1_ops)
        self.button2 = QPushButton("5V")
        self.button2.clicked.connect(self.button2_ops)
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.button1)
        buttonLayout.addWidget(self.button2)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.voltage)
        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)
        self.getVoltage.moveToThread(self.thread)
        self.getVoltage.data_signal.connect(self.updateValue)
        self.thread.started.connect(self.getVoltage.runWork)
        self.thread.start()

    def button1_ops(self):
        get_data, recv_data_buf = scpi_query(1, ':VOLTage 1.00\r\n')

    def button2_ops(self):
        get_data, recv_data_buf = scpi_query(1, ':VOLTage 5.00\r\n')

    def updateValue(self, volt):
        self.voltage.setText("Voltage: " + volt + " V")

    def __del__(self):
        self.thread.quit()
        self.thread.deleteLater()
        exit_all()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setWindowTitle("Power Python Demo")

    mainWindow.show()
    sys.exit(app.exec_())
