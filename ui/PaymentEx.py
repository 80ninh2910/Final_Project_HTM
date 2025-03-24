import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import QHeaderView

from librarys.CartManager import CartManager
from librarys.DataConnector import DataConnector
from librarys.PointManager import PointManager
from librarys.TransactionManager import TransactionManager
from librarys.UserSession import UserSession
from ui.BillEx import BillEx

from ui.Payment import Ui_MainWindow


class PaymentEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.mainwindow = None
        self.setupUi(self)
        self.final_total = 0

        self.cart = CartManager()
        self.dc = DataConnector()
        self.transaction_manager = TransactionManager()
        self.us = UserSession()
        self.point_manager = PointManager()  # Khởi tạo PointManager

        self.beverages = self.dc.bev
        self.popcorns = self.dc.pop
        self.combos = self.dc.com

        self.load_data()
        self.setup_connections()

        self.setWindowTitle("Check Transaction")
    def setup_connections(self):
        self.pushButtonfb.clicked.connect(self.open_facebook)
        self.pushButtonHome.clicked.connect(self.home)
        self.pushButtonConfirm.clicked.connect(self.confirm)
        self.pushButtonDiscounts.clicked.connect(self.open_discount)
        self.pushButtonAboutUs.clicked.connect(self.open_aboutus)

    def home(self):
        from ui.MainEx import MainEx
        self.mainwindow = MainEx()
        self.mainwindow.show()
        self.close()

    @staticmethod
    def open_facebook():
        QDesktopServices.openUrl(QUrl("https://www.facebook.com/profile.php?id=61573908070943"))
    def load_data(self):
        products = self.cart.cart.get("products", {})
        # Set up column headers and rows
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Name", "Quantity", "Price", "Total"]
        )
        if not products:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Cart is empty"))
            self.lineEditFinalPayment.setText("0 VND")
            return

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

        # Hiển thị tổng cộng
        self.tableWidget.setRowCount(row + 1)
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem("Total"))
        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{total} VND"))

        # Căn chỉnh kích thước cột để vừa với nội dung
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        seats = self.cart.get_seats()
        num_tickets = len(seats)
        self.labelTicket.setText(str(num_tickets))

        final_total = total + (num_tickets * 45000)
        self.lineEditFinalPayment.setText(f"{final_total} VND")

        if seats:
            info = next(iter(seats.values()))
            self.labelSeat.setText(", ".join(seats.keys()))
            self.labelTheater.setText(info.get("theater", "N/A"))
            self.labelTime.setText(info.get("showtime", "N/A"))

        info = self.us.get_user() or {}
        username = info.get("username", "N/A")
        email = info.get("email", "N/A")

        self.labelUsername.setText(username)
        self.labelMail.setText(email)

        # Hiển thị số điểm hiện có
        current_points = self.point_manager.get_points(username, email)
        self.lineEditShowPoint.setText(f"{current_points} Point")

    def confirm(self):

        seats = self.cart.get_seats() or {}
        products = self.cart.cart.get("products", {})

        total_products = sum(
            int(self.tableWidget.item(row, 3).text().replace(" VND", "").replace(",", ""))
            for row in range(self.tableWidget.rowCount() - 1)
            if self.tableWidget.item(row, 3)
        )

        # Get username and email from UI
        username = self.labelUsername.text()
        email = self.labelMail.text()
        # Get current points for the user
        current_points = self.point_manager.get_points(username, email)
        # Cho phép chọn số điểm sử dụng
        points_to_use, ok = QtWidgets.QInputDialog.getInt(self, "Use your point", "Enter Point", 0, 0,
                                                          current_points)
        if not ok:
            return
        # Calculate ticket and total price
        num_tickets = int(self.labelTicket.text().strip() or "0")
        total_tickets = num_tickets * 45000
        final_total = total_products + total_tickets
        # Calculate discount based on points used
        discount = self.point_manager.use_points(username, email, points_to_use)
        final_payment = max(0, final_total - discount)

        info = next(iter(seats.values()), {})
        theater = info.get("theater", "N/A")
        showtime = info.get("showtime", "N/A")

        user_info = self.us.get_user() or {}
        username = user_info.get("username", "N/A")
        email = user_info.get("email", "N/A")

        movie=self.cart.cart["movie"]

        self.open_bill(username,movie, theater,showtime, email, seats, products, final_payment)

    def open_bill(self, username,movie, theater, showtime, email, seats, products, final_payment):
        seat_text = ", ".join(seats.keys()) if seats else "Chưa đặt ghế nào"
        order_items = "\n".join(
            [f"- {name}: {quantity}x" for name, quantity in products.items() if quantity>0]
        ) or "Không có sản phẩm"

        self.bill_window = BillEx(self, username, email,movie, theater, showtime, seat_text, order_items, final_payment)
        self.bill_window.show()
        self.close()
    def clear_data(self):
        self.cart.clear_cart()
        self.load_data()
        self.reset_fields_payment()

    def reset_fields_payment(self):
        self.labelTicket.setText("")
        self.lineEditFinalPayment.setText("")
        self.labelSeat.setText("")
        self.labelTheater.setText("")
        self.labelTime.setText("")
        self.lineEditShowPoint.setText("")
        self.labelUsername.setText("")
        self.labelMail.setText("")
    def open_discount(self):
        from ui.DiscountEx import DiscountEx
        self.discount_window = DiscountEx()
        self.discount_window.show()
        self.close()

    def open_aboutus(self):
        from ui.AboutUsEx import AboutUsEx
        self.aboutus_window = AboutUsEx()
        self.aboutus_window.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PaymentEx()
    window.show()
    sys.exit(app.exec())