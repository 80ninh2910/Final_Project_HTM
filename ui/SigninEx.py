from PyQt6 import QtWidgets
import os

import sys

from libs.DataConnector import DataConnector
from ui.Signin import Ui_MainWindow  # Import giao diện từ Qt Designer

class SignInEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.dc=DataConnector()# Nút "Sign In"

    def login(self):
        username_or_email = self.lineEdit_2.text().strip()
        password = self.lineEdit_3.text().strip()

        valid_user=self.dc.login(username_or_email,password)
        if not os.path.exists(self.dc.cus):
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Không tìm thấy dữ liệu người dùng! Hãy đăng ký.")
            self.open_register_window()
            return



        # Kiểm tra tài khoản


        if valid_user:
            msg = QtWidgets.QMessageBox(self)
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setWindowTitle("Thành công")
            msg.setText("Đăng nhập thành công!")
            msg.setStyleSheet("QLabel{ color: black; } QWidget{ background-color: white; }")
            msg.exec()
            self.home()  # Gọi màn hình Main
        else:
            # Nếu không tìm thấy tài khoản, hiển thị lỗi và yêu cầu đăng ký
            QtWidgets.QMessageBox.warning(self, "Lỗi",
                                          "Tài khoản không tồn tại hoặc sai mật khẩu! Vui lòng kiểm tra lại.")

    def open_register_window(self):
        from ui.SignUpEx import SignUpEx

        if not hasattr(self, 'register_window') or self.register_window is None:
            self.register_window = SignUpEx()

        self.register_window.show()
        self.close()

    def home(self):
        from ui.MainEx import MainEx

        if not hasattr(self, 'mainwindow') or self.mainwindow is None:
            self.mainwindow = MainEx()

        self.mainwindow.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = SignInEx()
    login_window.show()
    sys.exit(app.exec())
