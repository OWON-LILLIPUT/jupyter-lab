from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QPushButton)
from PyQt5.QtChart import QChartView, QValueAxis, QLineSeries
from PyQt5.QtCore import *
from socket import *
import numpy as np
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


class GetOSCData(QtCore.QObject):
    data_signal = pyqtSignal(object)

    def __int__(self):
        super(GetOSCData, self).__int__()

    def runWork(self):
        while True:
            get_data, recv_data_buf = scpi_query(10, ':DATA:WAVE:SCREen:CH1?\r\n')
            if get_data:
                rec_scope_data_buf = recv_data_buf[4:]  # delete 4 length bytes
                scope_data_buf_int16 = np.frombuffer(rec_scope_data_buf, np.int16)
                self.data_signal.emit(scope_data_buf_int16)
            QThread.sleep(1)


class MainWindow(QWidget):
    getOSCData = GetOSCData()
    thread = QtCore.QThread()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setFixedSize(self.width(), self.height())

        set_up_tcp_client()

        self.qtChart = QChartView()

        self.x_Aix = QValueAxis()
        self.x_Aix.setRange(0, 1800)
        self.x_Aix.setLabelFormat("%f")
        self.x_Aix.setTickCount(10)
        self.x_Aix.setMinorTickCount(0)

        self.y_Aix = QValueAxis()
        self.y_Aix.setRange(-32000, 32000)
        self.y_Aix.setLabelFormat("%f")
        self.y_Aix.setTickCount(9)
        self.y_Aix.setMinorTickCount(0)

        self.series = QLineSeries()

        self._1_point_list = []
        for i in range(1800):
            self._1_point_list.append(QPointF(i, 0))
        self.series.append(self._1_point_list)

        self.qtChart.chart().setAxisX(self.x_Aix)
        self.qtChart.chart().setAxisY(self.y_Aix)
        self.qtChart.chart().setTitleBrush(QBrush(Qt.cyan))
        self.qtChart.chart().addSeries(self.series)

        self.series.attachAxis(self.x_Aix)
        self.series.attachAxis(self.y_Aix)

        self.button1 = QPushButton("100mV")
        self.button1.clicked.connect(self.button1_ops)
        self.button2 = QPushButton("1V")
        self.button2.clicked.connect(self.button2_ops)
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.button1)
        buttonLayout.addWidget(self.button2)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.qtChart)
        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)
        self.getOSCData.moveToThread(self.thread)
        self.getOSCData.data_signal.connect(self.updateValue)
        self.thread.started.connect(self.getOSCData.runWork)
        self.thread.start()

    def button1_ops(self):
        get_data, recv_data_buf = scpi_query(1, ':CH1:SCALe 100mV\r\n')

    def button2_ops(self):
        get_data, recv_data_buf = scpi_query(1, ':CH1:SCALe 1V\r\n')

    def updateValue(self, data_np):
        del self._1_point_list[len(self._1_point_list) - 1]
        self._1_point_list.insert(0, QPointF(0, data_np[0]))
        for i in range(0, len(self._1_point_list)):
            self._1_point_list[i].setX(i)
            self._1_point_list[i].setY(data_np[i])
        self.series.replace(self._1_point_list)

    def __del__(self):
        self.thread.quit()
        self.thread.deleteLater()
        exit_all()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setWindowTitle("OSC Python Demo")

    mainWindow.show()
    sys.exit(app.exec_())
