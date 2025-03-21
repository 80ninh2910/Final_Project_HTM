import sys

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QDesktopServices

from librarys.CartManager import CartManager
from librarys.DataConnector import DataConnector
from librarys.PointManager import PointManager
from librarys.TransactionManager import TransactionManager
from librarys.UserSession import UserSession
from models.Transaction import Transaction
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

        self.setWindowTitle("Xác nhận Thanh Toán")
    def setup_connections(self):
        self.pushButtonfb.clicked.connect(self.open_facebook)
        self.pushButtonHome.clicked.connect(self.home)
        self.pushButtonPay.clicked.connect(self.pay)

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
        self.tableWidget.clearContents()
        if not products:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Giỏ hàng trống"))
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

        self.tableWidget.setRowCount(row + 1)
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

        info = self.us.get_user() or {}
        username = info.get("username", "N/A")
        email = info.get("email", "N/A")

        self.labelUsername.setText(username)
        self.labelMail.setText(email)

        # Hiển thị số điểm hiện có
        current_points = self.point_manager.get_points(username, email)
        self.lineEditShowPoint.setText(f"{current_points} điểm")

    def pay(self):

        seats = self.cart.get_seats() or {}
        products = self.cart.cart.get("products", {})

        total_products = sum(
            int(self.tableWidget.item(row, 3).text().replace(" VND", "").replace(",", ""))
            for row in range(self.tableWidget.rowCount() - 1)
            if self.tableWidget.item(row, 3)
        )


        username = self.labelUsername.text()
        email = self.labelMail.text()
        current_points = self.point_manager.get_points(username, email)
        # Cho phép chọn số điểm sử dụng
        points_to_use, ok = QtWidgets.QInputDialog.getInt(self, "Dùng điểm", "Nhập số điểm muốn dùng:", 0, 0,
                                                          current_points)
        if not ok:
            return
        num_tickets = int(self.labelTicket.text().strip() or "0")
        total_tickets = num_tickets * 45000
        final_total = total_products + total_tickets

        discount = self.point_manager.use_points(username, email, points_to_use)
        final_payment = max(0, final_total - discount)

        seat_text = ", ".join(seats.keys()) if seats else "Chưa đặt ghế nào"
        info = next(iter(seats.values()), {})
        theater = info.get("theater", "N/A")
        showtime = info.get("showtime", "N/A")

        user_info = self.us.get_user() or {}
        username = user_info.get("username", "N/A")
        email = user_info.get("email", "N/A")

        order_items = "\n".join(
            [f"- {name}: {quantity}x" for name, quantity in products.items() if quantity > 0]) or "Chưa đặt hàng"

        transaction = Transaction(
            user_name=username,
            mail=email,
            theater=theater,
            showtime=showtime,
            seats=seat_text,
            num_tickets=num_tickets,
            order_items=order_items,
            price=final_payment
        )

        try:
            self.transaction_manager.save_transaction(transaction.to_dict())
        except Exception as e:
            print(f"Lỗi khi lưu giao dịch: {e}")
            return

         # Tạo QMessageBox
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle("Xác nhận Thanh Toán")
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Question)
        msg_box.setText(f"""
               Xác nhận Thanh Toán:
               - Người dùng: {username}
               - Email: {email}
               - Rạp chiếu: {theater}
               - Suất chiếu: {showtime}
               - Ghế: {seat_text}
               - Số vé: {num_tickets} (Tổng tiền vé: {total_tickets:,} VND)
               - Sản phẩm đã đặt:
               {order_items}
               
               
               - Tổng tiền sản phẩm: {total_products:,} VND
               --------------------------------
               Tổng tiền cuối cùng: {final_payment:,} VND
           """)

        # Load hình ảnh QR Code
        pixmap = QtGui.QPixmap("../images/qrcode.jpg").scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)
        label_image = QtWidgets.QLabel()
        label_image.setPixmap(pixmap)
        label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Layout chính chứa nội dung và hình ảnh
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(msg_box,alignment=Qt.AlignmentFlag.AlignCenter)  # Thêm nội dung tin nhắn
        layout.addWidget(label_image, alignment=Qt.AlignmentFlag.AlignCenter)  # Hình ảnh QR căn giữa

        # Tạo QDialog để chứa layout
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("QR Code Thanh Toán")
        dialog.setLayout(layout)

        # Thêm nút xác nhận và hủy
        btn_yes = msg_box.addButton("Yes", QtWidgets.QMessageBox.ButtonRole.AcceptRole)
        msg_box.addButton("No", QtWidgets.QMessageBox.ButtonRole.RejectRole)

        dialog.resize(400, 400)
        dialog.exec()

        if msg_box.clickedButton() == btn_yes:
            self.finalize_payment(final_payment)
            self.process_payment()

    def finalize_payment(self, final_payment):
        username = self.labelUsername.text()
        email = self.labelMail.text()
        self.point_manager.add_points(username, email, final_payment)  # Cộng điểm mới

        QtWidgets.QMessageBox.information(self, "Thanh Toán Thành Công", "Cảm ơn bạn đã mua vé!",
                                          QtWidgets.QMessageBox.StandardButton.Ok)
        self.cart.clear_cart()
        self.load_data()

    def process_payment(self):
        QtWidgets.QMessageBox.information(self, "Thanh Toán Thành Công", "Cảm ơn bạn đã mua vé!",
                                          QtWidgets.QMessageBox.StandardButton.Ok)
        self.cart.clear_cart()
        self.load_data()
        self.reset_fields()

    def reset_fields(self):
        self.labelTicket.setText("")
        self.lineEditFinalPayment.setText("")
        self.labelSeat.setText("")
        self.labelTheater.setText("")
        self.labelTime.setText("")
        self.lineEditShowPoint.setText("")
        self.labelUsername.setText("")
        self.labelMail.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PaymentEx()
    window.show()
    sys.exit(app.exec())