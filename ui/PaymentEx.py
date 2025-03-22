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
        """Khởi tạo giao diện thanh toán."""
        super().__init__()
        self.setupUi(self)
        self.mainwindow = None  # Cửa sổ chính
        self.final_total = 0  # Tổng tiền cuối cùng

        # Khởi tạo các đối tượng quản lý dữ liệu
        self.cart = CartManager()
        self.dc = DataConnector()
        self.transaction_manager = TransactionManager()
        self.us = UserSession()
        self.point_manager = PointManager()

        # Lấy danh sách sản phẩm
        self.beverages = self.dc.bev
        self.popcorns = self.dc.pop
        self.combos = self.dc.com

        self.load_data()
        self.setup_connections()
        self.setWindowTitle("Xác nhận giao dịch")

    def setup_connections(self):
        """Thiết lập kết nối các nút trong giao diện."""
        self.pushButtonfb.clicked.connect(self.open_facebook)
        self.pushButtonHome.clicked.connect(self.home)
        self.pushButtonConfirm.clicked.connect(self.confirm)

    def home(self):
        """Chuyển về màn hình chính."""
        from ui.MainEx import MainEx
        self.mainwindow = MainEx()
        self.mainwindow.show()
        self.close()

    @staticmethod
    def open_facebook():
        """Mở trang Facebook của ứng dụng."""
        QDesktopServices.openUrl(QUrl("https://www.facebook.com/profile.php?id=61573908070943"))

    def load_data(self):
        """Tải dữ liệu từ giỏ hàng và hiển thị trên giao diện."""
        products = self.cart.cart.get("products", {})
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Tên", "Số lượng", "Giá", "Tổng"])

        if not products:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Giỏ hàng trống"))
            self.lineEditFinalPayment.setText("0 VND")
            return

        total = 0
        row=0
        self.tableWidget.setRowCount(len(products))
        for (product_name, quantity) in products.items():
            if quantity == 0:
                continue
            price = self.dc.get_price(product_name)
            total += price * quantity
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(product_name))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(quantity)))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{price} VND"))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{price * quantity} VND"))
            row+=1



        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem("Tổng cộng"))
        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{total} VND"))


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

        user_info = self.us.get_user() or {}
        self.labelUsername.setText(user_info.get("username", "N/A"))
        self.labelMail.setText(user_info.get("email", "N/A"))
        self.lineEditShowPoint.setText(f"{self.point_manager.get_points(user_info.get('username', ''), user_info.get('email', ''))} Điểm")

    def confirm(self):
        """Xác nhận giao dịch và thanh toán."""
        seats = self.cart.get_seats() or {}
        products = self.cart.cart.get("products", {})

        total_products = sum(
            int(self.tableWidget.item(row, 3).text().replace(" VND", "").replace(",", ""))
            for row in range(self.tableWidget.rowCount() - 1)
            if self.tableWidget.item(row, 3)
        )

        user_info = self.us.get_user() or {}
        username, email = user_info.get("username", "N/A"), user_info.get("email", "N/A")
        current_points = self.point_manager.get_points(username, email)

        points_to_use, ok = QtWidgets.QInputDialog.getInt(self, "Sử dụng điểm", "Nhập số điểm", 0, 0, current_points)
        if not ok:
            return

        num_tickets = int(self.labelTicket.text().strip() or "0")
        total_tickets = num_tickets * 45000
        final_total = total_products + total_tickets
        discount = self.point_manager.use_points(username, email, points_to_use)
        final_payment = max(0, final_total - discount)

        info = next(iter(seats.values()), {})
        self.open_bill(username, info.get("theater", "N/A"), info.get("showtime", "N/A"), email, seats, products, final_payment)

    def open_bill(self, username, theater, showtime, email, seats, products, final_payment):
        """Mở cửa sổ hóa đơn thanh toán."""
        self.bill_window = BillEx(self, username, email, theater, showtime, ", ".join(seats.keys()) if seats else "Chưa đặt ghế nào",
                                  "\n".join([f"- {name}: {quantity}x" for name, quantity in products.items() if quantity > 0]) or "Không có sản phẩm",
                                  final_payment)
        self.bill_window.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PaymentEx()
    window.show()
    sys.exit(app.exec())
