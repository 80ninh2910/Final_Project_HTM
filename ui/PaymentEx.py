from PyQt6 import QtWidgets
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from librarys.CartManager import CartManager
from librarys.DataConnector import DataConnector
from ui.Payment import Ui_MainWindow

class PaymentEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.mainwindow = None
        self.setupUi(self)
        self.cart = CartManager()
        self.dc = DataConnector()
        self.beverages = self.dc.bev
        self.popcorns = self.dc.pop
        self.combos = self.dc.com

        self.load_data()
        self.setup_connections()

    def load_data(self):
        """Tải dữ liệu sản phẩm từ giỏ hàng và hiển thị trong bảng"""
        products = self.cart.cart["products"]
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(products))

        total = 0
        row = 0
        for product_name, quantity in products.items():
            if quantity == 0:
                continue
            price = self.dc.get_price(product_name)
            total += price * quantity
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(product_name))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(quantity)))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{price} VND"))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{price * quantity} VND"))
            row += 1

        # Thêm dòng tổng cộng
        self.tableWidget.setRowCount(row + 1)
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem("Tổng cộng"))
        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{total} VND"))

        # Hiển thị thông tin ghế và suất chiếu
        seats = self.cart.get_seats()
        if seats:
            info = next(iter(seats.values()))
            self.labelSeat.setText(", ".join(seats.keys()))
            self.labelTheater.setText(info["theater"])
            self.labelTime.setText(info["showtime"])

    def setup_connections(self):
        """Kết nối các sự kiện với nút bấm"""
        self.pushButtonfb.clicked.connect(self.open_facebook)
        self.pushButtonHome.clicked.connect(self.home)

    def home(self):
        """Quay lại màn hình chính"""
        from ui.MainEx import MainEx
        self.mainwindow = MainEx()
        self.mainwindow.show()
        self.close()

    @staticmethod
    def open_facebook():
        """Mở trang Facebook"""
        QDesktopServices.openUrl(QUrl("https://www.facebook.com/profile.php?id=61573908070943"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = PaymentEx()
    window.show()
    sys.exit(app.exec())