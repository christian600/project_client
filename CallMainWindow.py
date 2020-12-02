from UI.Ui_main import MainUI
from PyQt5 import QtWidgets
import Asset_pb2


class CallMainWindow(MainUI, QtWidgets.QMainWindow):
    def __init__(self, inet, signal, parent=None):
        super(CallMainWindow, self).__init__(parent)
        self.signal = signal
        self.inet = inet
        self.set_conn()

    def set_conn(self):
        self.left_button_2.clicked.connect(self.quit_click)
        self.signal.logout_rsp.connect(self.logout_rsp)

    def quit_click(self):
        logout_req = Asset_pb2.LogoutReq()
        logout_req.quit_flag = 2
        str_req = logout_req.SerializeToString()
        self.inet.send_msg(str_req, 2)

    def logout_rsp(self, msg):
        rsp = Asset_pb2.LogoutRsp()
        rsp.ParseFromString(msg[3])
        if (rsp.quit_flag == 2):
            self.close()
