from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import QUrl
from ui.Main import Ui_MainWindow




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
        self.pushButtonTrlexor.clicked.connect(lambda: self.open_youtube_video("https://www.youtube.com/watch?v=oDIvlcgq_FI"))
        self.pushButtonTrlfairytale.clicked.connect(
            lambda: self.open_youtube_video("https://www.youtube.com/watch?v=25NyBoZOoWc"))
        self.pushButtonTrdominion.clicked.connect(
            lambda: self.open_youtube_video("https://www.youtube.com/watch?v=PzaUMTOupJ8"))
        self.pushButtonfb.clicked.connect(lambda: self.open_youtube_video("https://www.facebook.com/profile.php?id=61573908070943"))
        self.pushButtonQNT.clicked.connect(self.openQNT)
        self.pushButtonNGT.clicked.connect(self.openNGT)
        self.pushButtonEMMA.clicked.connect(self.openEMMA)
        self.pushButtonDiscounts.clicked.connect(self.open_discount)
        self.pushButtonAboutUs.clicked.connect(self.open_aboutus)
        self.pushButtonLogOut.clicked.connect(self.logout)
    def logout(self):
        reply = QMessageBox.question(self, 'Confirm Logout', 'Are you sure you want to log out?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            from ui.SignUpEx import SignUpEx
            self.signup_win = SignUpEx()
            self.signup_win.show()
            self.close()
    @staticmethod
    def open_youtube_video(url):
        """Mở video hoặc đường dẫn trên trình duyệt"""
        qurl = QUrl(url)
        if qurl.isValid():
            QDesktopServices.openUrl(qurl)
        else:
            print(f"URL không hợp lệ: {url}")

    def openQNT(self):
        from ui.QNTEx import QNTEx
        self.qnt_window = QNTEx()
        self.qnt_window.show()
        self.close()

    def openNGT(self):
        from ui.NGTEx import NGTEx
        self.ngt_window = NGTEx()
        self.ngt_window.show()
        self.close()

    def openEMMA(self):
        from ui.EMMAEx import EMMAEx
        self.emma_window = EMMAEx()
        self.emma_window.show()
        self.close()
    def open_discount(self):
        from ui.DiscountEx import DiscountEx
        self.discount_window = DiscountEx()
        self.discount_window.show()
        self.close()

    def open_aboutus(self):
        from ui.AboutUsEx import AboutUsEx
        self.aboutus_window = AboutUsEx()
        self.aboutus_window.show()
        self.close()