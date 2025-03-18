from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QUrl
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
