from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import QMainWindow


from ui.AboutUs.AboutUs import Ui_MainWindow


class AboutUsEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Initialize UI
        self.setupSignalAndSlots()
        self.mainwindow=None
    def showWindow(self):
        self.show()  # Show this window properly

    def setupSignalAndSlots(self):
        self.pushButtonShowtimes.clicked.connect(self.home)
        self.pushButtonDiscounts.clicked.connect(self.open_discount)
        self.pushButtonBuyPop.clicked.connect(self.open_BuyPopcorn_Window)
        self.pushButtonfb.clicked.connect(self.openfb)
        self.pushButtonLearnMore1.clicked.connect(self.openfb)
        self.pushButtonLearnMore2.clicked.connect(self.openfb)
        self.pushButtonLearnMore3.clicked.connect(self.openfb)
        self.pushButtonLearnMore4.clicked.connect(self.openfb)


    def home(self):
        from ui.MainEx import MainEx

        if self.mainwindow is None:
            self.mainwindow = MainEx()

        self.mainwindow.show()
        self.close()

    def open_discount(self):
        from ui.Discount.DiscountEx import DiscountEx
        if self.mainwindow is None:
            self.mainwindow = DiscountEx()
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