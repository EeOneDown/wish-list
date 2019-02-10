import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindow import Ui_MainWindow
from itemWindow import Ui_MainWindow as Ui_ItemWindow


class ItemInfo(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_ItemWindow()
        self.ui.setupUi(self)


class MainWin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Wish List")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MainWin()
    myapp.show()
    sys.exit(app.exec_())
