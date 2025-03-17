from PyQt6 import QtWidgets
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices

from librarys.CartManager import CartManager
from librarys.DataConnector import DataConnector
from ui.Payment import Ui_MainWindow


class PaymentEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.cart = CartManager()
        self.dc=DataConnector()
        self.load_data()
        self.signalandslot()

        self.beverages = self.dc.bev
        self.popcorns = self.dc.pop
        self.combos = self.dc.com

    def load_data(self):

        products = self.cart.cart["products"]
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(products))
        total=0
        row = 0
        for product_name, quantity in products.items():
            if quantity==0:
                continue
            price=self.dc.get_price(product_name)
            total+=price*quantity
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(product_name))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(quantity)))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{price} VND"))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{price*quantity} VND"))
            row += 1
        self.tableWidget.setRowCount(row + 1)
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem("Tổng cộng"))
        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{total} VND"))

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
    sys.exit(app.exec())
