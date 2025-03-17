
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QUrl
from ui.Main import Ui_MainWindow
from ui.BuyPopcornEx import BuyPopcornEx
from ui.NGTEx import NGTEx
from ui.QNTEx import QNTEx

class MainEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Biến lưu trữ cửa sổ BuyPopcornEx
        self.buyPopcornWindow = None
        # Kết nối nút bấm để mở cửa sổ popcorn

        self.pushButtonTrlQNT.clicked.connect(self.open_youtube_videoQNT)
        self.pushButtonTrlNGT.clicked.connect(self.open_youtube_videoNGT)
        self.pushButtonTrEmma.clicked.connect(self.open_youtube_videoEmma)
        self.pushButtonfb.clicked.connect(self.openfb)
        self.pushButtonQNT.clicked.connect(self.openQNT)
        self.pushButtonNGT.clicked.connect(self.openNGT)
    def showWindow(self):
        self.show()


    #HÀM MỞ TRAILER TRÊN WEB
    def open_youtube_videoNGT(self):
        video_url = "https://www.youtube.com/watch?v=hXGozmNBwt4"
        QDesktopServices.openUrl(QUrl(video_url))
    def open_youtube_videoQNT(self):
        video_url = "https://www.youtube.com/watch?v=EB0nnm6akjA"
        QDesktopServices.openUrl(QUrl(video_url))
    def open_youtube_videoEmma(self):
        video_url = "https://www.youtube.com/watch?v=kraUpgr_IE4"
        QDesktopServices.openUrl(QUrl(video_url))
    def openfb(self):
        contact="https://www.facebook.com/profile.php?id=61573908070943"
        QDesktopServices.openUrl(QUrl(contact))
    def openQNT(self):
        self.qnt_window = QNTEx()
        self.qnt_window.show()
        self.close()
    def openNGT(self):
        self.ngt_window=NGTEx()
        self.ngt_window.show()
        self.close()