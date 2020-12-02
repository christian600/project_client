import INet
import DealMsg
from SendMsgSignal import SendMsgSignal
from CallLoginMainWin import CallLoginMainWin
from CallMainWindow import CallMainWindow


class Manage:
    def __init__(self):
        self.signal = SendMsgSignal()
        self.deal_msg = DealMsg.DealMsg(self.signal)
        self.inet = INet.INet(self.deal_msg)
        self.main_win = CallMainWindow(self.inet, self.signal)
        self.login_win = CallLoginMainWin(self.inet, self.signal,
                                          self.main_win)

    def init(self):
        self.inet.init()

    def run(self):
        self.inet.run()
        self.login_win.show()
