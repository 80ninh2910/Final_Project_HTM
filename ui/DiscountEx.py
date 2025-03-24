from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import QMainWindow

from ui.Discount import Ui_MainWindow


class DiscountEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Initialize UI
        self.setupSignalAndSlots()
        self.mainwindow=None
    def showWindow(self):
        self.show()  # Show this window properly

    def setupSignalAndSlots(self):
        self.pushButtonShowtimes.clicked.connect(self.home)
        self.pushButtonAboutUs.clicked.connect(self.open_aboutus)
        self.pushButtonBuyPop.clicked.connect(self.open_BuyPopcorn_Window)
        self.pushButtonGetTK1.clicked.connect(self.home)
        self.pushButtonGetTK2.clicked.connect(self.home)
        self.pushButtonSeeShowtimes.clicked.connect(self.home)
        self.pushButtonfb.clicked.connect(self.openfb)
        self.pushButtonPlanYourVisit.clicked.connect(self.home)
        self.pushButtonSeeShowtimes.clicked.connect(self.home)
        self.pushButtonJoinInsider.clicked.connect(self.JoinInsider)
        self.pushButtonSeeMorePromotions.clicked.connect(self.openfb)
        self.pushButtonTicket_2.clicked.connect(self.home)
    def home(self):
        from ui.MainEx import MainEx

        if self.mainwindow is None:
            self.mainwindow = MainEx()

        self.mainwindow.show()
        self.close()

    def open_aboutus(self):
        from ui.AboutUsEx import AboutUsEx
        if self.mainwindow is None:
            self.mainwindow = AboutUsEx()

        self.mainwindow.show()
        self.close()

    def open_BuyPopcorn_Window(self):
        from ui.BuyPopcornEx import BuyPopcornEx
        if self.mainwindow is None:
            self.mainwindow = BuyPopcornEx()
        self.mainwindow.show()
        self.close()
    def openfb(self):
        contact="https://www.facebook.com/profile.php?id=61573908070943"
        QDesktopServices.openUrl(QUrl(contact))
    def JoinInsider(self):
        pass