import INet
import DealMsg


class Manage:
    def __init__(self):
        self.deal_msg = DealMsg.DealMsg()
        self.inet = INet.INet(self.deal_msg)

    def init(self):
        self.inet.init()

    def run(self):
        self.inet.run()


manager = Manage()
manager.init()
manager.run()
buff = "hello world"
manager.inet.send_msg(buff, 1)
