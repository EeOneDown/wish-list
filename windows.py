from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox
from mainWindow import Ui_MainWindow
from itemWindow import Ui_MainWindow as Ui_ItemWindow
from interfaces import WishInterface
from models import session
from sqlalchemy.exc import IntegrityError


class ItemInfo(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_ItemWindow()
        self.ui.setupUi(self)

        self.wish = None

        self.ui.saveBtn.clicked.connect(self._on_save_clicked)
        self.ui.deleteBtn.clicked.connect(self._on_delete_clicked)

    def set_new(self):
        self.setWindowTitle("New Wish")

    def set_from_item(self, item: QListWidgetItem):
        _id = int(item.text().split(". ")[0])
        self.wish = self.parent().WishInterface.get(_id)

        self.setWindowTitle(f"Wish: {self.wish.title}")
        
        self.ui.titleLE.setText(self.wish.title)
        self.ui.priceLE.setText(self.wish.price)
        self.ui.linkLE.setText(self.wish.link)
        self.ui.descriptionLE.setText(self.wish.description)

    def _raise_msg(self, text: str):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setText(text)
        msg.setWindowTitle("Warning!")
        msg.show()

    def _on_save_clicked(self):
        if not self.ui.titleLE.text():
            return self._raise_msg("Empty title!")

        if self.ui.priceLE.text():
            try:
                float(self.ui.priceLE.text())
            except ValueError:
                return self._raise_msg("Price must be float!")
            if float(self.ui.priceLE.text()) < 0:
                return self._raise_msg("Price must be >= 0!")

        if not self.wish:
            try:
                self.parent().WishInterface.create(
                    self.ui.titleLE.text(),
                    self.ui.priceLE.text() or None,
                    self.ui.linkLE.text() or None,
                    self.ui.descriptionLE.text() or None
                )
            except IntegrityError:
                self.parent().WishInterface.session.rollback()
                return self._raise_msg(
                    f"Wish \"{self.ui.titleLE.text()}\" already exist!"
                )
        else:
            self.wish.title = self.ui.titleLE.text()
            self.wish.price = self.ui.priceLE.text()
            self.wish.link = self.ui.linkLE.text()
            self.wish.description = self.ui.descriptionLE.text()
            self.parent().WishInterface.update(self.wish)
        self.close()

        self.parent().update()

    def _on_delete_clicked(self):
        if self.wish:
            self.parent().WishInterface.delete(self.wish)
        self.close()

        self.parent().update()


class MainWin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Wish List")
        self.WishInterface = WishInterface(session)

        self.items = []
        self.update()

        self.ui.itemsLW.itemDoubleClicked.connect(self._on_item_clicked)
        self.ui.createBtn.clicked.connect(self._on_create_clicked)
        self.ui.deleteAllBtn.clicked.connect(self._on_delete_clicked)

    def _on_item_clicked(self, item: QListWidgetItem):
        self.current_item = ItemInfo(self)
        self.current_item.set_from_item(item)
        self.current_item.show()

    def _on_create_clicked(self):
        self.current_item = ItemInfo(self)
        self.current_item.set_new()
        self.current_item.show()

    def _on_delete_clicked(self):
        for wish in self.WishInterface.all():
            self.WishInterface.delete(wish)

        self.update()

    def update(self, *__args):
        while len(self.items):
            self.ui.itemsLW.takeItem(0)
            self.items.pop(0)

        wishes = self.WishInterface.all()
        self.items = [f"{wish.id}. {wish.title}" for wish in wishes]
        self.ui.itemsLW.addItems(self.items)
