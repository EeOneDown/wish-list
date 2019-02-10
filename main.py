import sys
from PyQt5.QtWidgets import QApplication
from windows import MainWin


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MainWin()
    myapp.show()
    sys.exit(app.exec_())
