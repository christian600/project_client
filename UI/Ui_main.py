import qdarkstyle
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QSplitter, QStackedLayout, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent, QCursor, QPainter
from PyQt5.QtChart import QChartView, QLineSeries, QChart
import sys
from PyQt5.QtWidgets import QApplication


class MainUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)
        self.init_ui()
        self.left_add_init()
        self.right_down_add_init()

    def init_ui(self):
        self.resize(900, 600)
        self.setWindowOpacity(0.9)
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        self.left_frame = QtWidgets.QFrame()
        self.left_frame.setObjectName("left_frame")
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_layout = QtWidgets.QGridLayout()
        self.left_frame.setLayout(self.left_layout)

        self.right_up_frame = QtWidgets.QFrame()
        self.right_up_frame.setObjectName("right_up_frame")
        self.right_up_frame.setFrameShape(QFrame.StyledPanel)
        self.right_up_layout = QStackedLayout()
        self.right_up_frame.setLayout(self.right_up_layout)

        self.right_down_frame = QtWidgets.QFrame()
        self.right_down_frame.setObjectName("right_down_frame")
        self.right_down_frame.setFrameShape(QFrame.StyledPanel)
        self.right_down_layout = QtWidgets.QGridLayout()
        self.right_down_frame.setLayout(self.right_down_layout)
        '''
        self.right_down_frame.setLayout(self.right_down_layout)
        self.main_layout.addWidget(self.left_frame, 0, 0, 12, 2)
        self.main_layout.addWidget(self.right_up_frame, 0, 2, 7, 10)
        self.main_layout.addWidget(self.right_down_frame, 7, 2, 5, 10)
        '''

        self.splitter1 = QSplitter(Qt.Vertical)
        self.splitter1.addWidget(self.right_up_frame)
        self.splitter1.addWidget(self.right_down_frame)
        self.splitter1.setSizes([400, 300])

        self.splitter2 = QSplitter(Qt.Horizontal)
        self.splitter2.addWidget(self.left_frame)
        self.splitter2.addWidget(self.splitter1)
        self.splitter2.setSizes([200, 800])
        self.main_layout.addWidget(self.splitter2)

        self.setCentralWidget(self.main_widget)

    def left_add_init(self):
        self.left_button_1 = QtWidgets.QPushButton("个人信息")
        self.left_button_1.setObjectName('left_button_1')
        self.left_layout.addWidget(self.left_button_1, 0, 0, 1, 1)
        self.left_button_2 = QtWidgets.QPushButton("退出")
        self.left_button_2.setObjectName('left_button_2')
        self.left_layout.addWidget(self.left_button_2, 1, 0, 2, 1)

    def right_down_add_init(self):
        self.chart = QChart()
        self.chart.setTitle("Line Chart 1")
        series = QLineSeries(self.chart)
        
        series.append(0, 6)
        series.append(2, 4)
        self.chart.addSeries(series)
        self.chart.setBackgroundVisible(False)
        self.chart.createDefaultAxes()  # 创建默认轴
        self.view = QChartView(self.chart)
        self.view.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.right_down_layout.addWidget(self.view, 0, 0, 1, 1)
        series.append(1, 4)
        
        

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainUI()
    main.show()
    sys.exit(app.exec_())

