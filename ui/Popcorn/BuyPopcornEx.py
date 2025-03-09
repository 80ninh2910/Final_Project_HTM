from PyQt6.QtWidgets import QMainWindow

from ui.Popcorn.BuyPopcorn import Ui_MainWindow


class BuyPopcornEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Initialize UI
        self.setupSignalAndSlots()
        self.mainwindow=None
    def showWindow(self):
        self.show()  # Show this window properly

    def setupSignalAndSlots(self):
        self.pushButtonHome.clicked.connect(self.home)
    def home(self):
        from ui.Main.MainEx import MainEx

        if self.mainwindow is None:
            self.mainwindow = MainEx()

        self.mainwindow.show()
        self.close()