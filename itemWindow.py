# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'itemWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 250)
        MainWindow.setMinimumSize(QtCore.QSize(415, 250))
        MainWindow.setMaximumSize(QtCore.QSize(415, 250))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBtn.setGeometry(QtCore.QRect(170, 190, 101, 41))
        self.deleteBtn.setObjectName("deleteBtn")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(290, 190, 101, 41))
        self.saveBtn.setObjectName("saveBtn")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(30, 20, 67, 17))
        self.titleLabel.setObjectName("titleLabel")
        self.priceLabel = QtWidgets.QLabel(self.centralwidget)
        self.priceLabel.setGeometry(QtCore.QRect(30, 100, 67, 17))
        self.priceLabel.setObjectName("priceLabel")
        self.linkLabel = QtWidgets.QLabel(self.centralwidget)
        self.linkLabel.setGeometry(QtCore.QRect(250, 20, 67, 17))
        self.linkLabel.setObjectName("linkLabel")
        self.descriptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.descriptionLabel.setGeometry(QtCore.QRect(250, 100, 111, 17))
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.titleLE = QtWidgets.QLineEdit(self.centralwidget)
        self.titleLE.setGeometry(QtCore.QRect(20, 50, 151, 31))
        self.titleLE.setObjectName("titleLE")
        self.linkLE = QtWidgets.QLineEdit(self.centralwidget)
        self.linkLE.setGeometry(QtCore.QRect(240, 50, 151, 31))
        self.linkLE.setObjectName("linkLE")
        self.descriptionLE = QtWidgets.QLineEdit(self.centralwidget)
        self.descriptionLE.setGeometry(QtCore.QRect(240, 130, 151, 31))
        self.descriptionLE.setObjectName("descriptionLE")
        self.priceLE = QtWidgets.QLineEdit(self.centralwidget)
        self.priceLE.setGeometry(QtCore.QRect(20, 130, 151, 31))
        self.priceLE.setObjectName("priceLE")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.deleteBtn.setText(_translate("MainWindow", "Удалить"))
        self.saveBtn.setText(_translate("MainWindow", "Сохранить"))
        self.titleLabel.setText(_translate("MainWindow", "Название"))
        self.priceLabel.setText(_translate("MainWindow", "Цена"))
        self.linkLabel.setText(_translate("MainWindow", "Ссылка"))
        self.descriptionLabel.setText(_translate("MainWindow", "Примечание"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
