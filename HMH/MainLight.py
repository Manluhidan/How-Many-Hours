# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainLight.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainScreenLight(object):
    def setupUi(self, MainScreenLight):
        MainScreenLight.setObjectName("MainScreenLight")
        MainScreenLight.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainScreenLight)
        self.centralwidget.setObjectName("centralwidget")
        self.bgwidget = QtWidgets.QWidget(self.centralwidget)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255))}")
        self.bgwidget.setObjectName("bgwidget")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 160, 301, 51))
        self.label_2.setStyleSheet("font: 11pt \"Microsoft YaHei UI\";;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(139, 164, 203, 255), stop:1 rgba(97, 136, 186, 255));")
        self.label_2.setObjectName("label_2")
        self.Add_bot = QtWidgets.QPushButton(self.bgwidget)
        self.Add_bot.setGeometry(QtCore.QRect(250, 250, 281, 61))
        self.Add_bot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(139, 164, 203, 255), stop:1 rgba(97, 136, 186, 255));\n"
"border-radius:20px;\n"
"font: 24pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.Add_bot.setObjectName("Add_bot")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(170, 70, 451, 61))
        self.label.setStyleSheet("font: 40pt \"Microsoft YaHei UI\";;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(139, 164, 203, 255), stop:1 rgba(97, 136, 186, 255));")
        self.label.setObjectName("label")
        self.Done_bot = QtWidgets.QPushButton(self.bgwidget)
        self.Done_bot.setGeometry(QtCore.QRect(250, 320, 281, 61))
        self.Done_bot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(164, 191, 239, 255), stop:1 rgba(106, 147, 203, 255));\n"
"border-radius:20px;\n"
"font: 24pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.Done_bot.setObjectName("Done_bot")
        self.num = QtWidgets.QDoubleSpinBox(self.bgwidget)
        self.num.setGeometry(QtCore.QRect(270, 200, 231, 31))
        self.num.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";")
        self.num.setMaximum(240.59)
        self.num.setObjectName("num")
        self.Dark_bot = QtWidgets.QPushButton(self.bgwidget)
        self.Dark_bot.setGeometry(QtCore.QRect(710, 500, 81, 41))
        self.Dark_bot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(139, 164, 203, 255), stop:1 rgba(97, 136, 186, 255));\n"
"border-radius:20px;\n"
"font: 10pt \"Microsoft YaHei UI\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));")
        self.Dark_bot.setObjectName("Dark_bot")
        MainScreenLight.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainScreenLight)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainScreenLight.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainScreenLight)
        self.statusbar.setObjectName("statusbar")
        MainScreenLight.setStatusBar(self.statusbar)

        self.retranslateUi(MainScreenLight)
        QtCore.QMetaObject.connectSlotsByName(MainScreenLight)

    def retranslateUi(self, MainScreenLight):
        _translate = QtCore.QCoreApplication.translate
        MainScreenLight.setWindowTitle(_translate("MainScreenLight", "MainWindow"))
        self.label_2.setText(_translate("MainScreenLight", "Enter video duration ( Minutes.Seconds )"))
        self.Add_bot.setText(_translate("MainScreenLight", "Add"))
        self.label.setText(_translate("MainScreenLight", "How Many Hours"))
        self.Done_bot.setText(_translate("MainScreenLight", "Done"))
        self.Dark_bot.setText(_translate("MainScreenLight", "Dark Mode"))
