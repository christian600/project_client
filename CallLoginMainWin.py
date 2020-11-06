import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from UI.Ui_login import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

import Asset_pb2

class CallLoginMainWin(QMainWindow, Ui_MainWindow):
    def __init__(self, inet, signal, parent=None):
        super(CallLoginMainWin, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.inet = inet
        self.signal = signal
        self.set_qss()
        self.setupUi(self)
        self.init()
        self.set_conn()
        
    def init(self):
        self.lbl_bg_of_login.setPixmap(QtGui.QPixmap("./image/login_bg.jpg"))
        self.lbl_bg_of_login.setScaledContents(True)
        self.setFixedSize(self.width(),self.height())
        
    def set_conn(self):
        self.btn_login_close.clicked.connect(self.close)
        self.btn_confrim_login.clicked.connect(self.login_click)
        self.signal.log_rsp.connect(self.login_rsp)

    def login_click(self):
        login_rsq = Asset_pb2.LoginReq()
        login_rsq.id = 20201
        login_rsq.password = "first_test"
        str_rsp = login_rsq.SerializeToString()
        self.inet.send_msg(str_rsp, 1)

    def login_rsp(self, msg):
        log_rsp = Asset_pb2.LoginRsp()
        log_rsp.ParseFromString(msg[3])
        self.edit_name_of_user.setText(log_rsp.rsp)

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
'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_win = CallLoginMainWin()
    login_win.show()
    sys.exit(app.exec_())
'''