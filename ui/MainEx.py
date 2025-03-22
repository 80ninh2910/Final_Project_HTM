from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QUrl

from ui.EMMAEx import EMMAEx
from ui.Main import Ui_MainWindow
from ui.NGTEx import NGTEx
from ui.QNTEx import QNTEx

class MainEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buyPopcornWindow = None  # Cửa sổ mua bắp rang
        self.setupConnections()

