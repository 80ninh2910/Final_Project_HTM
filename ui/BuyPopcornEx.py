from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from librarys.CartManager import CartManager
from librarys.DataConnector import DataConnector
from ui.BuyPopcorn import Ui_MainWindow

class BuyPopcornEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignalAndSlots()
        self.mainwindow = None
        self.data_connector = DataConnector()
        self.beverages = self.data_connector.bev  # Lấy danh sách đồ uống
        self.popcorns = self.data_connector.pop  # Lấy danh sách bắp rang
        self.combos = self.data_connector.com  # Lấy danh sách combo
        self.cm = CartManager()  # Giỏ hàng
        self.setup_cart()

