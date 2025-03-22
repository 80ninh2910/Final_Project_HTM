from PyQt6 import QtWidgets

from ui.Bill import Ui_MainWindow

class BillEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, username, email, theater, showtime, seat_text, order_items, total_price):
        super().__init__()
        self.setupUi(self)
        self.set_data(username, email, theater, showtime, seat_text, order_items, total_price)

    def set_data(self, username, email, theater, showtime, seat_text, order_items, total_price):
        self.labelUsername.setText(username)
        self.labelMail.setText(email)
        self.labelTheater.setText(theater)
        self.labelTime.setText(showtime)
        self.labelSeat.setText(seat_text)
        self.labelOrder.setText(order_items)
        self.labelTotal.setText(f"{total_price} VND")