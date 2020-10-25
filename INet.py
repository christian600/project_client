import socket
import threading
HOST = "49.233.184.31"
PORT = 12100
IP_PORT = (HOST, PORT)


class MyThread(threading.Thread):
    def __init__(self, threadID, name, exit_flag, sock, deal_msg):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.exit_flag = exit_flag
        self.sock = sock
        self.deal_msg = deal_msg

    def run(self):
        self.recv_sock_data()

    def recv_sock_data(self):
        while self.exit_flag > 0:
            data = self.sock.recv(1024)
            recv_msg = self.deal_msg.deal_recv_data(data)
            if (recv_msg[1] == 1):
                self.exit_flag = 0
            self.deal_msg.deal_msg(recv_msg)


class INet:
    def __init__(self, deal_msg):
        self.deal_msg = deal_msg

    def init(self):
        self.init_sock()
        self.init_thread()

    def init_sock(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(IP_PORT)

    def init_thread(self):
        self.mythread = MyThread(1, 'recv_thread', 1, self.sock, self.deal_msg)

    def run(self):
        self.mythread.start()

    def send_msg(self, data, data_type):
        send_data = self.deal_msg.set_data(data, data_type)
        self.sock.send(send_data)
