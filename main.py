import Asset_pb2
import Manager
import CallLoginMainWin
import sys

if __name__ == "__main__":
    manager = Manager.Manage()
    manager.init()
    app = CallLoginMainWin.QApplication(sys.argv)
    login_win = CallLoginMainWin.CallLoginMainWin(manager.inet, manager.signal)
    login_win.show()
    manager.run()
    sys.exit(app.exec_())
    
    