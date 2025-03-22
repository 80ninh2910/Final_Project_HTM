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

    def showWindow(self):
        """Hiển thị cửa sổ chính"""
        self.show()

    def setupConnections(self):
        """Thiết lập các sự kiện click cho các nút bấm"""
        self.pushButtonTrlQNT.clicked.connect(lambda: self.open_youtube_video("https://www.youtube.com/watch?v=EB0nnm6akjA"))
        self.pushButtonTrlNGT.clicked.connect(lambda: self.open_youtube_video("https://www.youtube.com/watch?v=hXGozmNBwt4"))
        self.pushButtonTrEmma.clicked.connect(lambda: self.open_youtube_video("https://www.youtube.com/watch?v=kraUpgr_IE4"))
        self.pushButtonfb.clicked.connect(lambda: self.open_youtube_video("https://www.facebook.com/profile.php?id=61573908070943"))
        self.pushButtonQNT.clicked.connect(self.openQNT)
        self.pushButtonNGT.clicked.connect(self.openNGT)
        self.pushButtonEMMA.clicked.connect(self.openEMMA)
        self.pushButtonDiscounts.clicked.connect(self.open_discount)
        self.pushButtonAboutUs.clicked.connect(self.open_aboutus)

    @staticmethod
    def open_youtube_video(url):
        """Mở video hoặc đường dẫn trên trình duyệt"""
        QDesktopServices.openUrl(QUrl(url))

    def openQNT(self):
        """Mở cửa sổ phim Quỷ Nhập Tràng"""
        self.qnt_window = QNTEx()
        self.qnt_window.show()
        self.close()

    def openNGT(self):
        """Mở cửa sổ phim Nhà Gia Tiên"""
        self.ngt_window = NGTEx()
        self.ngt_window.show()
        self.close()

    def openEMMA(self):
        self.ngt_window = EMMAEx()
        self.ngt_window.show()
        self.close()
    def open_discount(self):
        from ui.Discount.DiscountEx import DiscountEx
        if self.mainwindow is None:
            self.mainwindow = DiscountEx()
        self.mainwindow.show()
        self.close()

    def open_aboutus(self):
        from ui.AboutUs.AboutUsEx import AboutUsEx
        if self.mainwindow is None:
            self.mainwindow = AboutUsEx()
        self.mainwindow.show()
        self.close()