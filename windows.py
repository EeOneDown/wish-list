from PyQt5.QtWidgets import QMainWindow
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
