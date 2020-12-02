from PyQt5.QtCore import pyqtSignal, QObject


class SendMsgSignal(QObject):
    log_rsp = pyqtSignal(tuple)
    logout_rsp = pyqtSignal(tuple)