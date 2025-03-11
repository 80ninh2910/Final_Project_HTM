from PyQt6.QtWidgets import QMainWindow

from ui.Main import Ui_MainWindow
from ui.BuyPopcornEx import BuyPopcornEx

class MainEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Biến lưu trữ cửa sổ BuyPopcornEx
        self.buyPopcornWindow = None

        # Kết nối nút bấm để mở cửa sổ popcorn
        self.pushButtonBuyPop.clicked.connect(self.open_BuyPopcorn_Window)
    def showWindow(self):
        self.show()
    def open_BuyPopcorn_Window(self):
        """ Mở cửa sổ BuyPopcornEx và đóng MainEx """
        if self.buyPopcornWindow is None:  # Chỉ tạo nếu chưa có
            self.buyPopcornWindow = BuyPopcornEx()

        self.buyPopcornWindow.show()  # Hiển thị cửa sổ BuyPopcornEx
        self.close()  # Đóng cửa sổ MainEx