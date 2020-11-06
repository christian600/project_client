import struct

class DealMsg:
    def __init__(self, signal):
        self.signal = signal
        self.func_dict = {}
        self.init_map()

    def set_data(self, buff, buff_type):
        buff_size = len(buff)
        msg_type = buff_type
        msg_size = 12 + buff_size
        msg_format = '<3i{0}s'.format(buff_size)
        data = struct.pack(msg_format, msg_size, msg_type, buff_size,
                           buff)
        return data

    def deal_recv_data(self, byte_data):
        msg_format = '<3i{0}s'.format(len(byte_data) - 12)
        recv_msg = struct.unpack(msg_format, byte_data)
        return recv_msg
        # self.deal_msg(recv_msg)

    def init_map(self):
        # 将type与具体的处理函数做映射
        self.func_dict[1] = self.Login_return
        pass

    def deal_msg(self, msg):
        # msg包含了type与buff， 通过表驱动， 调用具体的处理函数
        self.func_dict[msg[1]](msg)

    def Login_return(self, msg):
        self.signal.log_rsp.emit(msg)