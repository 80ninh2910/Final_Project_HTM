import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from librarys.CartManager import CartManager
from librarys.DataConnector import DataConnector
from librarys.UserSession import UserSession
from ui.EMMA import Ui_MainWindow

class SeatSelectionWindow(QtWidgets.QDialog):
    def __init__(self, theater, showtime, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Chọn Ghế - {theater} ({showtime})")
        self.theater = theater
        self.showtime = showtime
        self.selected_seats = set()
        self.initUI()

