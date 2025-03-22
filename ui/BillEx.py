

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt


from librarys.PointManager import PointManager
from librarys.TransactionManager import TransactionManager
from models.Transaction import Transaction
from ui.Bill import Ui_MainWindow

class BillEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,payment_window, username, email, theater, showtime, seat_text, order_items, final_payment):
        super().__init__()
        self.setupUi(self)
        self.payment_window = payment_window
        self.transaction_manager = TransactionManager()
        self.point_manager = PointManager()
        self.final_payment = final_payment

        self.set_data(username, email, theater, showtime, seat_text, order_items, final_payment)
        self.pushButtonPay.clicked.connect(self.pay)
        self.pushButtonBack.clicked.connect(self.back)

    def set_data(self, username, email, theater, showtime, seat_text, order_items, final_payment):
        self.labelUsername.setText(username)
        self.labelMail.setText(email)
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
        showtime = self.labelTime.text()
        seat_text = self.labelSeat.text()
        order_items = self.labelOrder.text()
        final_payment = int(self.labelTotal.text().replace(" VND", "").replace(",", ""))

        # Create transaction object
        transaction = Transaction(
            user_name=username,
            mail=email,
            theater=theater,
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
        # Dialog for confirmation with a QR code
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("QR Code Thanh Toán")

        # Load the QR code image
        pixmap = QtGui.QPixmap("../images/qrcode.jpg")
        if not pixmap.isNull():
            pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "QR code image not found.")
            return

        # Create a label for the QR code
        label_image = QtWidgets.QLabel()
        label_image.setPixmap(pixmap)
        label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create a layout and add the image and buttons
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label_image)

        # Yes/No buttons
        button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.StandardButton.Yes | QtWidgets.QDialogButtonBox.StandardButton.No)
        layout.addWidget(button_box)

        button_box.accepted.connect(lambda: self.handle_success(dialog, self.final_payment))  # Yes
        button_box.rejected.connect(dialog.reject)  # No

        dialog.setLayout(layout)
        dialog.resize(300, 300)
        dialog.exec()
    def handle_success(self, dialog,final_payment):
        QtWidgets.QMessageBox.information(self, "Payment Successful", "Payment Successful!")
        self.finalize_payment(final_payment)
        self.process_payment()
        dialog.accept()  # Close the dialog
    def finalize_payment(self, final_payment):
        username = self.labelUsername.text()
        email = self.labelMail.text()
        self.point_manager.add_points(username, email, final_payment)  # Cộng điểm mới
        self.payment_window.clear_data()
        self.payment_window.load_data()
    def process_payment(self):
        QtWidgets.QMessageBox.information(self, "Payment Successful", "Thank you for purchasing your ticket!",
                                          QtWidgets.QMessageBox.StandardButton.Ok)
        self.reset_fields_bill()
        self.payment_window.clear_data()
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
