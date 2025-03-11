from PyQt6 import QtWidgets
import os
import json
import sys
from ui.Signin import Ui_MainWindow  # Import giao diện từ Qt Designer

class SignInEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)  # Nút "Sign In"

    def login(self):
        username_or_email = self.lineEdit_2.text().strip()
        password = self.lineEdit_3.text().strip()

        user_file = "../database/customers.json"
        if not os.path.exists(user_file):
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Không tìm thấy dữ liệu người dùng! Hãy đăng ký.")
            self.open_register_window()
            return

        # Đọc dữ liệu từ JSON
        customers = []
        try:
            with open(user_file, "r", encoding="utf-8") as f:
                customers = json.load(f)
        except json.JSONDecodeError as e:
            QtWidgets.QMessageBox.warning(self, "Lỗi", f"File JSON bị lỗi định dạng: {str(e)}")
            return
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Lỗi", f"Lỗi khi đọc dữ liệu: {str(e)}")
            return

        # Kiểm tra tài khoản
        for user in customers:
            if (user.email == username_or_email for user in customers )or (user.username == username_or_email for user in customers) and user.password ==password:
                msg = QtWidgets.QMessageBox(self)
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setWindowTitle("Thành công")
                msg.setText("Đăng nhập thành công!")
                msg.setStyleSheet("QLabel{ color: black; } QWidget{ background-color: white; }")
                msg.exec()
                self.home()  # Gọi màn hình Main
                return

        # Nếu không tìm thấy tài khoản, chuyển sang đăng ký
        QtWidgets.QMessageBox.warning(self, "Lỗi", "Tài khoản không tồn tại! Vui lòng đăng ký.")
        self.open_register_window()

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
