# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DoneLight.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DoneLight(object):
    def setupUi(self, DoneLight):
        DoneLight.setObjectName("DoneLight")
        DoneLight.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(DoneLight)
        self.centralwidget.setObjectName("centralwidget")
        self.bgwidget = QtWidgets.QWidget(self.centralwidget)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255))}")
        self.bgwidget.setObjectName("bgwidget")
        self.Normal_bot = QtWidgets.QPushButton(self.bgwidget)
        self.Normal_bot.setGeometry(QtCore.QRect(250, 110, 281, 61))
        self.Normal_bot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(139, 164, 203, 255), stop:1 rgba(97, 136, 186, 255));\n"
"border-radius:20px;\n"
"font: 24pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.Normal_bot.setObjectName("Normal_bot")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(170, 20, 451, 61))
        self.label.setStyleSheet("font: 40pt \"Microsoft YaHei UI\";;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(139, 164, 203, 255), stop:1 rgba(97, 136, 186, 255));")
        self.label.setObjectName("label")
        self.Exit_bot = QtWidgets.QPushButton(self.bgwidget)
        self.Exit_bot.setGeometry(QtCore.QRect(250, 470, 281, 61))
        self.Exit_bot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(164, 191, 239, 255), stop:1 rgba(106, 147, 203, 255));\n"
"border-radius:20px;\n"
"font: 24pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.Exit_bot.setObjectName("Exit_bot")
        self.Dark_bot = QtWidgets.QPushButton(self.bgwidget)
        self.Dark_bot.setGeometry(QtCore.QRect(710, 500, 81, 41))
        self.Dark_bot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(139, 164, 203, 255), stop:1 rgba(97, 136, 186, 255));\n"
"border-radius:20px;\n"
"font: 10pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.Dark_bot.setObjectName("Dark_bot")
        self.Quarter_bot = QtWidgets.QPushButton(self.bgwidget)
        self.Quarter_bot.setGeometry(QtCore.QRect(250, 180, 281, 61))
        self.Quarter_bot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(139, 164, 203, 255), stop:1 rgba(97, 136, 186, 255));\n"
"border-radius:20px;\n"
"font: 24pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.Quarter_bot.setObjectName("Quarter_bot")
        self.Half_bot = QtWidgets.QPushButton(self.bgwidget)
        self.Half_bot.setGeometry(QtCore.QRect(250, 250, 281, 61))
        self.Half_bot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(139, 164, 203, 255), stop:1 rgba(97, 136, 186, 255));\n"
"border-radius:20px;\n"
"font: 24pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.Half_bot.setObjectName("Half_bot")
        self.ThreeQuarters_bot = QtWidgets.QPushButton(self.bgwidget)
        self.ThreeQuarters_bot.setGeometry(QtCore.QRect(250, 320, 281, 61))
        self.ThreeQuarters_bot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(139, 164, 203, 255), stop:1 rgba(97, 136, 186, 255));\n"
"border-radius:20px;\n"
"font: 24pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.ThreeQuarters_bot.setObjectName("ThreeQuarters_bot")
        self.Double_bot = QtWidgets.QPushButton(self.bgwidget)
        self.Double_bot.setGeometry(QtCore.QRect(250, 390, 281, 61))
        self.Double_bot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(139, 164, 203, 255), stop:1 rgba(97, 136, 186, 255));\n"
"border-radius:20px;\n"
"font: 24pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.Double_bot.setObjectName("Double_bot")
        self.Return_bot = QtWidgets.QPushButton(self.bgwidget)
        self.Return_bot.setGeometry(QtCore.QRect(710, 450, 81, 41))
        self.Return_bot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(139, 164, 203, 255), stop:1 rgba(97, 136, 186, 255));\n"
"border-radius:20px;\n"
"font: 10pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.Return_bot.setObjectName("Return_bot")
        DoneLight.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DoneLight)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        DoneLight.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DoneLight)
        self.statusbar.setObjectName("statusbar")
        DoneLight.setStatusBar(self.statusbar)

        self.retranslateUi(DoneLight)
        QtCore.QMetaObject.connectSlotsByName(DoneLight)

    def retranslateUi(self, DoneLight):
        _translate = QtCore.QCoreApplication.translate
        DoneLight.setWindowTitle(_translate("DoneLight", "MainWindow"))
        self.Normal_bot.setText(_translate("DoneLight", "Normal Speed"))
        self.label.setText(_translate("DoneLight", "How Many Hours"))
        self.Exit_bot.setText(_translate("DoneLight", "Exit"))
        self.Dark_bot.setText(_translate("DoneLight", "Dark Mode"))
        self.Quarter_bot.setText(_translate("DoneLight", "1.25 Speed"))
        self.Half_bot.setText(_translate("DoneLight", "1.5 Speed"))
        self.ThreeQuarters_bot.setText(_translate("DoneLight", "1.75 Speed"))
        self.Double_bot.setText(_translate("DoneLight", "2 Speed"))
        self.Return_bot.setText(_translate("DoneLight", "Return"))