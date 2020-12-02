from PyQt5.QtWidgets import QMainWindow
from UI.Ui_login import Ui_MainWindow
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent, QCursor
import Asset_pb2


class CallLoginMainWin(QMainWindow, Ui_MainWindow):
    def __init__(self, inet, signal, main_win, parent=None):
        super(CallLoginMainWin, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.inet = inet
        self.signal = signal
        self.main_win = main_win
        self.set_qss()
        self.setupUi(self)
        self.init()
        self.set_conn()

    def init(self):
        self.lbl_bg_of_login.setPixmap(QtGui.QPixmap("./image/login_bg.jpg"))
        self.lbl_bg_of_login.setScaledContents(True)
        self.setFixedSize(self.width(), self.height())

    def set_conn(self):
        self.btn_login_close.clicked.connect(self.quit_click)
        self.btn_confrim_login.clicked.connect(self.login_click)
        self.signal.log_rsp.connect(self.login_rsp)
        self.signal.logout_rsp.connect(self.logout_rsp)

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

    def login_click(self):
        login_rsq = Asset_pb2.LoginReq()
        if self.edit_name_of_user.text() == "" or self.edit_pwd_of_user.text() == "":
            self.lbl_login_warning.setText("请输入用户名或密码")
            return
        login_rsq.id = int(self.edit_name_of_user.text())
        login_rsq.password = self.edit_pwd_of_user.text()
        str_rsp = login_rsq.SerializeToString()
        self.inet.send_msg(str_rsp, 1)

    def quit_click(self):
        logout_req = Asset_pb2.LogoutReq()
        logout_req.quit_flag = 1
        str_req = logout_req.SerializeToString()
        self.inet.send_msg(str_req, 2)

    def login_rsp(self, msg):
        log_rsp = Asset_pb2.LoginRsp()
        log_rsp.ParseFromString(msg[3])
        if (log_rsp.code != 1):
            self.lbl_login_warning.setText("用户名或密码错误")
            return
        self.main_win.show()
        self.close()

    def logout_rsp(self, msg):
        rsp = Asset_pb2.LogoutRsp()
        rsp.ParseFromString(msg[3])
        if (rsp.quit_flag == 1):
            self.close()

    def set_qss(self):
        self.qss_style = '''
            #btn_login_close, #btn_register{
                border:none;
            }
            #btn_confrim_login{
                color:White;
                border-radius: 7px;
                font-family:微软雅黑;
                background:#6633FF;
                border:1px;
                }
            #btn_confrim_login:hover{
                background:#6666FF;
                }
            #btn_confrim_login:pressed{
                background:#6600FF;
                }
            #edit_name_of_user{
                background: #f3f3f3;
                background-image: url(./image/user_login.png);
                background-repeat: no-repeat;
                background-position: left;
                color: black;
                padding: 5 5 5 30;
                border-color: black;
                border-style:solid;
                border-top-width:0px;
                border-right-width:0px;
                border-bottom-width:1px;
                border-left-width:0px;}
            #edit_pwd_of_user{
                background: #f3f3f3;
                background-image: url(./image/login_pwd.jpg);
                background-repeat: no-repeat;
                background-position: left;
                color: black;
                padding: 3 3 3 30;
                border-color: black;
                border-style:solid;
                border-top-width:0px;
                border-right-width:0px;
                border-bottom-width:1px;
                border-left-width:0px;}
        '''
        self.setStyleSheet(self.qss_style)
