from PyQt6 import QtWidgets
import sys
import os
import json
from librarys.JSON_File_Factory import JsonFileFactory
from models.Customer import Customer
from ui.SigninEx import SignInEx
from ui.SignUp import Ui_MainWindow

class SignUpEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.login_window = None
        self.setupUi(self)
        self.jff = JsonFileFactory()
        self.customer_file = "../database/Customers.json"

        # Kết nối sự kiện cho các nút
        self.pushButtonSignUp.clicked.connect(self.save_user)  # Nút "SIGN UP"
        self.pushButtonSignIn.clicked.connect(self.switch_to_signin)  # Nút "Sign In Now!!!"

    def save_user(self):
        """Lưu thông tin đăng ký người dùng"""
        email = self.lineEditGmail.text().strip()
        username = self.lineEditUsername.text().strip()
        password = self.lineEditPw.text().strip()
        confirm_password = self.lineEditRePw.text().strip()
        is_agreed = self.radioButtonAgree.isChecked()  # Kiểm tra checkbox đồng ý

        if not is_agreed:
            self.show_message("Lỗi", "Bạn phải đồng ý với điều khoản để tiếp tục đăng ký!", QtWidgets.QMessageBox.Icon.Warning)
            return

        if not email or not username or not password or not confirm_password:
            self.show_message("Lỗi", "Vui lòng nhập đầy đủ thông tin!", QtWidgets.QMessageBox.Icon.Warning)
            return

        if password != confirm_password:
            self.show_message("Lỗi", "Mật khẩu xác nhận không khớp!", QtWidgets.QMessageBox.Icon.Warning)
            return

        customers = self.load_customers()
        if any(user.email == email for user in customers):
            self.show_message("Lỗi", "Email đã được đăng ký!", QtWidgets.QMessageBox.Icon.Warning)
            return

        new_customer = Customer(email=email, username=username, password=password)
        customers.append(vars(new_customer))

        if self.save_customers(customers):
            self.show_message("Thành công", "Đăng ký thành công!", QtWidgets.QMessageBox.Icon.Information)
            self.switch_to_signin()

    def load_customers(self):
        """Tải danh sách khách hàng từ file JSON"""
        if os.path.exists(self.customer_file):
            try:
                return self.jff.read_data(self.customer_file, Customer) or []
            except (json.JSONDecodeError, Exception):
                return []
        return []

    def save_customers(self, customers):
        """Lưu danh sách khách hàng vào file JSON"""
        try:
            self.jff.write_data(customers, self.customer_file)
            return True
        except Exception:
            return False

    def switch_to_signin(self):
        """Chuyển sang màn hình đăng nhập"""
        self.login_window = SignInEx()
        self.login_window.show()
        self.close()

    @staticmethod
    def show_message(title, text, icon):
        """Hiển thị thông báo"""
        msg = QtWidgets.QMessageBox()
        msg.setIcon(icon)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setStyleSheet("QLabel{ color: black; } QWidget{ background-color: white; }")
        msg.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    signup_window = SignUpEx()
    signup_window.show()
    sys.exit(app.exec())
