import Manager
import Asset_pb2

if __name__ == "__main__":
    manager = Manager.Manage()
    manager.init()
    manager.run()
    login_rsq = Asset_pb2.LoginReq()
    login_rsq.id = "322026"
    login_rsq.password = "h"
    str_rsp = login_rsq.SerializeToString()
    manager.inet.send_msg(str_rsp, 1)