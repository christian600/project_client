import Manager
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = Manager.Manage()
    manager.init()
    manager.run()
    sys.exit(app.exec_())
