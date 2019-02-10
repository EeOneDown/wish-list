# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.itemsLW = QtWidgets.QListWidget(self.centralwidget)
        self.itemsLW.setGeometry(QtCore.QRect(10, 10, 781, 531))
        self.itemsLW.setObjectName("itemsLW")
        self.createBtn = QtWidgets.QPushButton(self.centralwidget)
        self.createBtn.setGeometry(QtCore.QRect(18, 550, 101, 41))
        self.createBtn.setObjectName("createBtn")
        self.deleteAllBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteAllBtn.setGeometry(QtCore.QRect(140, 550, 101, 41))
        self.deleteAllBtn.setObjectName("deleteAllBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.createBtn.setText(_translate("MainWindow", "Создать"))
        self.deleteAllBtn.setText(_translate("MainWindow", "Удалить все"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
