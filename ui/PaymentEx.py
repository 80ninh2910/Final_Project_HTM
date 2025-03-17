from PyQt6 import QtWidgets
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices

from librarys.CartManager import CartManager
from ui.Payment import Ui_MainWindow


class PaymentEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.cart = CartManager()
        self.load_data()
        self.signalandslot()

    def load_data(self):

        seats=self.cart.get_seats()
        info=next(iter(seats.values()))
        theater = info["theater"]
        showtime = info["showtime"]
        seat_text = ", ".join(seats.keys())

        self.labelSeat.setText(str(seat_text))
        self.labelTheater.setText(str(theater))
        self.labelTime.setText(str(showtime))

    def signalandslot(self):
        self.pushButtonfb.clicked.connect(self.openfb)
        self.pushButtonHome.clicked.connect(self.home)

    def home(self):
        from ui.MainEx import MainEx
        self.mainwindow = MainEx()
        self.mainwindow.show()
        self.close()
    def openfb(self):
        contact="https://www.facebook.com/profile.php?id=61573908070943"
        QDesktopServices.openUrl(QUrl(contact))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = PaymentEx()
    window.show()
    window.load_data()
    sys.exit(app.exec())
