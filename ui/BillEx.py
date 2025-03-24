

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt


from librarys.PointManager import PointManager
from librarys.QRFactory import PaymentMethodFactory
from librarys.TransactionManager import TransactionManager
from models.Transaction import Transaction
from ui.Bill import Ui_MainWindow

class PaymentSelectionDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Chọn phương thức thanh toán")
        self.setStyleSheet("background-color: white;")

        # Tạo danh sách radio button
        self.payment_methods = {
            "Momo": "momo",
            "VNPay": "vnpay",
            "VietQR": "vietqr"
        }
        self.selected_method = None  # Lưu phương thức đã chọn

        layout = QtWidgets.QVBoxLayout()

        self.radio_buttons = {}
        for name, method in self.payment_methods.items():
            radio = QtWidgets.QRadioButton(name)
            self.radio_buttons[method] = radio
            layout.addWidget(radio)

        # Nút Xác nhận
        self.confirm_button = QtWidgets.QPushButton("Xác nhận")
        self.confirm_button.clicked.connect(self.accept_selection)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def accept_selection(self):
        for method, radio in self.radio_buttons.items():
            if radio.isChecked():
                self.selected_method = method
                break
        self.accept()  # Đóng dialog

class BillEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,payment_window, username, email,movie, theater, showtime, seat_text, order_items, final_payment):
        super().__init__()
        self.setupUi(self)
        self.payment_window = payment_window
        self.transaction_manager = TransactionManager()
        self.point_manager = PointManager()
        self.final_payment = final_payment

        self.set_data(username, email,movie, theater, showtime, seat_text, order_items, final_payment)
        self.pushButtonPay.clicked.connect(self.pay)
        self.pushButtonBack.clicked.connect(self.back)

        self.payment=PaymentMethodFactory()

    def set_data(self, username, email,movie, theater, showtime, seat_text, order_items, final_payment):
        self.labelUsername.setText(username)
        self.labelMail.setText(email)
        self.labelMovie.setText(movie)
        self.labelTheater.setText(theater)
        self.labelTime.setText(showtime)
        self.labelSeat.setText(seat_text)
        self.labelOrder.setText(order_items)
        self.labelTotal.setText(f"{final_payment} VND")
    def pay(self):
        # Retrieve data from labels to pass to the Transaction model
        username = self.labelUsername.text()
        email = self.labelMail.text()
        theater = self.labelTheater.text()
        movie = self.labelMovie.text()
        showtime = self.labelTime.text()
        seat_text = self.labelSeat.text()
        order_items = self.labelOrder.text()
        final_payment = int(self.labelTotal.text().replace(" VND", "").replace(",", ""))

        # Create transaction object
        transaction = Transaction(
            user_name=username,
            mail=email,
            theater=theater,
            movie=movie,
            showtime=showtime,
            seats=seat_text,
            order_items=order_items,
            price=final_payment
        )

        try:
            self.transaction_manager.save_transaction(transaction.to_dict())
        except Exception as e:
            print(f"Lỗi khi lưu giao dịch: {e}")
            return

        # Show QR Code dialog with Yes/No buttons
        self.show_qr_code()

    def show_qr_code(self):
        'Hiển thị dialog chọn phương thức thanh toán'
        dialog = PaymentSelectionDialog(self)
        if dialog.exec():
            selected_method = dialog.selected_method

            # Lấy QR tương ứng
            payment_method = self.payment.get_qr(selected_method)
            pixmap = QtGui.QPixmap(payment_method.display_qr())

            # Hiển thị QR code trong dialog
            qr_dialog = QtWidgets.QDialog(self)
            qr_dialog.setWindowTitle("QR Code Thanh Toán")
            qr_dialog.setStyleSheet("background-color: white;")

            label_image = QtWidgets.QLabel()
            label_image.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))
            label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(label_image)

            # Thêm nút xác nhận thanh toán
            button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.StandardButton.Yes |
                                                    QtWidgets.QDialogButtonBox.StandardButton.No)
            layout.addWidget(button_box)

            button_box.accepted.connect(lambda: self.handle_success(qr_dialog, self.final_payment))
            button_box.rejected.connect(qr_dialog.reject)

            qr_dialog.setLayout(layout)
            qr_dialog.resize(300, 300)
            qr_dialog.exec()

    def handle_success(self, dialog,final_payment):
        QtWidgets.QMessageBox.information(self, "Payment Successful", "Payment Successful!")
        self.finalize_payment(final_payment)
        self.process_payment()
        dialog.accept()  # Close the dialog
    def finalize_payment(self, final_payment):
        username = self.labelUsername.text()
        email = self.labelMail.text()
        self.point_manager.add_points(username, email, final_payment)  # Cộng điểm mới
    def process_payment(self):
        QtWidgets.QMessageBox.information(self, "Payment Successful", "Thank you for purchasing your ticket!",
                                          QtWidgets.QMessageBox.StandardButton.Ok)
        self.reset_fields_bill()
        self.payment_window.clear_data()
        self.payment_window.close()
        self.close()
        from ui.MainEx import MainEx
        self.main_window = MainEx()
        self.main_window.show()
    def reset_fields_bill(self):
        self.labelUsername.setText("")
        self.labelMail.setText("")
        self.labelTheater.setText("")
        self.labelTime.setText("")
        self.labelSeat.setText("")
        self.labelOrder.setText("")
        self.labelTotal.setText("")

    def back(self):
        self.payment_window.show()  # Reuse the existing PaymentEx window
        self.close()
