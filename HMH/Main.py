import sys
import HMH
from MainLight import Ui_MainScreenLight
from DoneLight import Ui_DoneLight
from MainDark import Ui_MainScreenDark
from DoneDark import Ui_DoneDark
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QMainWindow, QMessageBox, QFileDialog


class MainLight(QMainWindow, Ui_MainScreenLight):
    def __init__(self):
        super(MainLight, self).__init__()
        self.setupUi(self)
        self.Dark_bot.clicked.connect(self.gotomaindark)
        self.Add_bot.clicked.connect(self.Add)
        self.Done_bot.clicked.connect(self.Done)

    def gotomaindark(self):
        page = MainDark()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotodonelight(self):
        page = DoneLight()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Add(self):
        num = self.num.value()
        if num > 0:
            HMH.count += 1
            HMH.values += num
            msg = QMessageBox()
            msg.setWindowTitle("Add")
            msg.setWindowIcon(QIcon('HMH.png'))
            msg.setText(f"Video number {HMH.count} has been added.")
            msg.setIcon(QMessageBox.Information)
            run = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Add")
            msg.setWindowIcon(QIcon('HMH.png'))
            msg.setText("Video duration cannot be 0.")
            msg.setIcon(QMessageBox.Critical)
            run = msg.exec_()

    def Done(self):
        if HMH.count == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Done")
            msg.setWindowIcon(QIcon('HMH.png'))
            msg.setText("There are no videos")
            msg.setIcon(QMessageBox.Critical)
            run = msg.exec_()
        else:
            self.gotodonelight()

class MainDark(QMainWindow, Ui_MainScreenDark):
    def __init__(self):
        super(MainDark, self).__init__()
        self.setupUi(self)
        self.Light_bot.clicked.connect(self.gotomainlight)
        self.Add_bot.clicked.connect(self.Add)
        self.Done_bot.clicked.connect(self.Done)

    def gotomainlight(self):
        page = MainLight()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotodonedark(self):
        page = DoneDark()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Add(self):
        num = self.num.value()
        if num > 0:
            HMH.count += 1
            HMH.values += num
            msg = QMessageBox()
            msg.setWindowTitle("Add")
            msg.setWindowIcon(QIcon('HMH.png'))
            msg.setText(f"Video number {HMH.count} has been added.")
            msg.setIcon(QMessageBox.Information)
            run = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Add")
            msg.setWindowIcon(QIcon('HMH.png'))
            msg.setText("Video duration cannot be 0.")
            msg.setIcon(QMessageBox.Critical)
            run = msg.exec_()

    def Done(self):
        if HMH.count == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Done")
            msg.setWindowIcon(QIcon('HMH.png'))
            msg.setText("There are no videos")
            msg.setIcon(QMessageBox.Critical)
            run = msg.exec_()
        else:
            self.gotodonedark()

class DoneLight(QMainWindow, Ui_DoneLight):
    def __init__(self):
        super(DoneLight, self).__init__()
        self.setupUi(self)
        self.Normal_bot.clicked.connect(self.normal)
        self.Quarter_bot.clicked.connect(self.quarter)
        self.Half_bot.clicked.connect(self.half)
        self.ThreeQuarters_bot.clicked.connect(self.threeQuarters)
        self.Double_bot.clicked.connect(self.double)
        self.Return_bot.clicked.connect(self.gotomainlight)
        self.Dark_bot.clicked.connect(self.gotodonedark)
        self.Exit_bot.clicked.connect(self.exit)

    def normal(self):
        msg = QMessageBox()
        msg.setWindowTitle("Add")
        msg.setWindowIcon(QIcon('HMH.png'))
        msg.setText(HMH.normal())
        msg.setIcon(QMessageBox.Information)
        run = msg.exec_()

    def quarter(self):
        msg = QMessageBox()
        msg.setWindowTitle("Add")
        msg.setWindowIcon(QIcon('HMH.png'))
        msg.setText(HMH.quarter())
        msg.setIcon(QMessageBox.Information)
        run = msg.exec_()

    def half(self):
        msg = QMessageBox()
        msg.setWindowTitle("Add")
        msg.setWindowIcon(QIcon('HMH.png'))
        msg.setText(HMH.half())
        msg.setIcon(QMessageBox.Information)
        run = msg.exec_()

    def threeQuarters(self):
        msg = QMessageBox()
        msg.setWindowTitle("Add")
        msg.setWindowIcon(QIcon('HMH.png'))
        msg.setText(HMH.threeQuarters())
        msg.setIcon(QMessageBox.Information)
        run = msg.exec_()

    def double(self):
        msg = QMessageBox()
        msg.setWindowTitle("Add")
        msg.setWindowIcon(QIcon('HMH.png'))
        msg.setText(HMH.double())
        msg.setIcon(QMessageBox.Information)
        run = msg.exec_()

    def gotodonedark(self):
        page = DoneDark()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotomainlight(self):
        page = MainLight()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def exit(self):
        sys.exit(app.exec_())

class DoneDark(QMainWindow, Ui_DoneDark):
    def __init__(self):
        super(DoneDark, self).__init__()
        self.setupUi(self)
        self.Normal_bot.clicked.connect(self.normal)
        self.Quarter_bot.clicked.connect(self.quarter)
        self.Half_bot.clicked.connect(self.half)
        self.ThreeQuarters_bot.clicked.connect(self.threeQuarters)
        self.Double_bot.clicked.connect(self.double)
        self.Return_bot.clicked.connect(self.gotomaindark)
        self.Dark_bot.clicked.connect(self.gotodonelight)
        self.Exit_bot.clicked.connect(self.exit)

    def normal(self):
        msg = QMessageBox()
        msg.setWindowTitle("Add")
        msg.setWindowIcon(QIcon('HMH.png'))
        msg.setText(HMH.normal())
        msg.setIcon(QMessageBox.Information)
        run = msg.exec_()

    def quarter(self):
        msg = QMessageBox()
        msg.setWindowTitle("Add")
        msg.setWindowIcon(QIcon('HMH.png'))
        msg.setText(HMH.quarter())
        msg.setIcon(QMessageBox.Information)
        run = msg.exec_()

    def half(self):
        msg = QMessageBox()
        msg.setWindowTitle("Add")
        msg.setWindowIcon(QIcon('HMH.png'))
        msg.setText(HMH.half())
        msg.setIcon(QMessageBox.Information)
        run = msg.exec_()

    def threeQuarters(self):
        msg = QMessageBox()
        msg.setWindowTitle("Add")
        msg.setWindowIcon(QIcon('HMH.png'))
        msg.setText(HMH.threeQuarters())
        msg.setIcon(QMessageBox.Information)
        run = msg.exec_()

    def double(self):
        msg = QMessageBox()
        msg.setWindowTitle("Add")
        msg.setWindowIcon(QIcon('HMH.png'))
        msg.setText(HMH.double())
        msg.setIcon(QMessageBox.Information)
        run = msg.exec_()

    def gotodonelight(self):
        page = DoneLight()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotomaindark(self):
        page = MainDark()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def exit(self):
        sys.exit(app.exec_())

app = QApplication(sys.argv)
MS = MainLight()
widget = QStackedWidget()
widget.setWindowTitle('How many hours')
widget.setWindowIcon(QIcon('HMH.png'))
widget.addWidget(MS)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")