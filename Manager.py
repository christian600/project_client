import INet
import DealMsg
from SendMsgSignal import SendMsgSignal

class Manage:
    def __init__(self):
        self.signal = SendMsgSignal()
        self.deal_msg = DealMsg.DealMsg(self.signal)
        self.inet = INet.INet(self.deal_msg)

    def init(self):
        self.inet.init()

    def run(self):
        self.inet.run()
