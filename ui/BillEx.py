

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

