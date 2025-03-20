import json

from PyQt6 import QtWidgets
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from librarys.CartManager import CartManager, PricingManager
from librarys.DataConnector import DataConnector
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

        self.beverages = self.dc.bev
        self.popcorns = self.dc.pop
        self.combos = self.dc.com

        self.us=UserSession()

        self.load_data()
        self.setup_connections()

    def load_data(self):
        """Tải dữ liệu sản phẩm từ giỏ hàng và hiển thị trong bảng"""
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

        # Thêm dòng tổng cộng
        self.tableWidget.setRowCount(row + 1)
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem("Tổng cộng"))
        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{total} VND"))

        # Lấy thông tin ghế đặt
        seats = self.cart.get_seats()
        num_tickets = len(seats)  # Mỗi ghế tương ứng với một vé

        # Hiển thị số vé trên labelTicket
        self.labelTicket.setText(str(num_tickets))

        # Tính tổng tiền cuối cùng (bao gồm vé)
        final_total = total + (num_tickets * 45000)
        self.lineEditFinalPayment.setText(f"{final_total} VND")

        # Cập nhật thông tin điểm tích lũy vào lineEditShowPoint
        #self.lineEditShowPoint.setText(str(self.current_customer.points))


        # Hiển thị thông tin ghế và suất chiếu
        seats = self.cart.get_seats()
        if seats:
            info = next(iter(seats.values()))
            self.labelSeat.setText(", ".join(seats.keys()))
            self.labelTheater.setText(info["theater"])
            self.labelTime.setText(info["showtime"])

        info=self.us.get_user()
        self.labelUsername.setText(str(info["username"]))
        self.labelMail.setText(str(info["email"]))

    def setup_connections(self):
        """Kết nối các sự kiện với nút bấm"""
        self.pushButtonfb.clicked.connect(self.open_facebook)
        self.pushButtonHome.clicked.connect(self.home)
        self.pushButtonPay.clicked.connect(self.pay)


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

    def pay(self):
        seats = self.cart.get_seats()
        products = self.cart.cart.get("products", {})

        # Lấy thông tin về tổng tiền sản phẩm từ bảng (cột cuối cùng)
        total_products = 0
        row_count = self.tableWidget.rowCount()
        for row in range(row_count - 1):  # Không tính dòng "Tổng cộng"
            total_value_item = self.tableWidget.item(row, 3)
            if total_value_item:
                total_value = total_value_item.text().replace(" VND", "").replace(",", "")
                total_products += int(total_value)

        # Lấy thông tin tổng số ghế và tính tiền vé (đã tính trong hàm load_data)
        num_tickets = int(self.labelTicket.text())
        ticket_price = 45000
        total_tickets = num_tickets * ticket_price

        # Tính tổng tiền cuối cùng
        final_total = total_products + total_tickets

        # Lấy thông tin ghế
        if seats:
            seat_text = ", ".join(seats.keys())
            infor = next(iter(seats.values()))
            num_tickets = len(seats)  # Mỗi ghế = 1 vé
            theater = infor.get("theater", "N/A")
            showtime = infor.get("showtime", "N/A")
        else:
            seat_text = "Chưa đặt ghế nào"
            num_tickets = 0
            theater = "N/A"
            showtime = "N/A"

        # Lấy thông tin người dùng
        info = self.us.get_user()
        if info:  # Kiểm tra nếu info không phải là None
            username = info.get("username", "N/A")
            email = info.get("email", "N/A")
        else:
            username = "N/A"
            email = "N/A"

        # Lấy thông tin bắp nước (chỉ lấy sản phẩm có số lượng > 0)
        order_items = "\n".join([f"- {name}: {quantity}x" for name, quantity in products.items() if quantity > 0])
        if not order_items:
            order_items = "Chưa đặt hàng"

        transaction = Transaction(
            user_name=username,
            mail=email,
            theater=theater,
            showtime=showtime,
            seats=seat_text,
            num_tickets=num_tickets,
            order_items=order_items,
            price=final_total
        )

        # Lưu lịch sử giao dịch
        self.transaction_manager.save_transaction(transaction.to_dict())

        # Hiển thị QMessageBox với 2 nút Thanh Toán / Từ Chối
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Xác nhận Thanh Toán")
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(json.dumps(transaction.to_dict(), indent=4, ensure_ascii=False))

        msg.setText(f"""
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
           Tổng tiền cuối cùng: {final_total:,} VND
           """)

        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        # Kiểm tra nút có tồn tại không trước khi đặt tên
        yes_button = msg.button(QtWidgets.QMessageBox.StandardButton.Yes)
        no_button = msg.button(QtWidgets.QMessageBox.StandardButton.No)

        if yes_button:
            yes_button.setText("Thanh Toán")
        if no_button:
            no_button.setText("Từ Chối")

        response = msg.exec()

        if response == QtWidgets.QMessageBox.StandardButton.Yes:
            self.process_payment()

    def process_payment(self):
        """Xử lý thanh toán: chỉ xóa giỏ hàng và xác nhận thanh toán."""
        QtWidgets.QMessageBox.information(self, "Thanh Toán Thành Công", "Cảm ơn bạn đã mua vé!",
                                          QtWidgets.QMessageBox.StandardButton.Ok)

        self.cart.clear_cart()  # Xóa giỏ hàng sau khi thanh toán
        self.load_data()  # Cập nhật lại giao diện giỏ hàng (hiển thị giỏ hàng trống)
        self.reset_fields()

    def reset_fields(self):
        self.labelTicket.setText("")
        self.lineEditFinalPayment.setText("")
        self.lineEditShowPoint.setText("")
        self.labelSeat.setText("")
        self.labelTheater.setText("")
        self.labelTime.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = PaymentEx()
    window.show()
    sys.exit(app.exec())