from PyQt6 import QtWidgets
import sys
from librarys.DataConnector import DataConnector
from librarys.UserSession import UserSession

from ui.Signin import Ui_MainWindow

class SignInEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.mainwindow = None
        self.register_window = None
        self.setupUi(self)
        self.dc = DataConnector()
        self.pushButton.clicked.connect(self.login)# Nút "Sign In"
        self.pushButtonSignUp.clicked.connect(self.signup)
        self.us=UserSession()
    def signup(self):
        from ui.SignUpEx import SignUpEx
        self.signip_win=SignUpEx()
        self.signip_win.show()
        self.close()
    def login(self):
        """Xử lý đăng nhập"""
        username_or_email = self.lineEdit_2.text().strip()
        password = self.lineEdit_3.text().strip()

        valid_user = self.dc.login(username_or_email, password)
        if valid_user:
            self.us.set_user(username_or_email)
            self.show_message("Success", "Login successful!!!", QtWidgets.QMessageBox.Icon.Information)
            self.home()
        else:
            self.show_message("Error", "Email has already been registered!", QtWidgets.QMessageBox.Icon.Warning)

    def home(self):
        """Chuyển sang màn hình chính"""
        from ui.MainEx import MainEx
        self.mainwindow = MainEx()
        self.mainwindow.show()
        self.close()

    def open_register_window(self):
        """Mở cửa sổ đăng ký"""
        from ui.SignUpEx import SignUpEx
        self.register_window = SignUpEx()
        self.register_window.show()
        self.close()

    @staticmethod
    def show_message(title, text, icon):
        """Hiển thị thông báo"""
        msg = QtWidgets.QMessageBox()
        msg.setIcon(icon)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setStyleSheet("QLabel{ color: black; } QWidget{ background-color: white;color: black; }")
        msg.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = SignInEx()
    login_window.show()
    sys.exit(app.exec())
