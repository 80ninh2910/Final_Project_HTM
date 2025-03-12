from PyQt6 import QtWidgets
import sys
import os
import json
from libs.JSON_File_Factory import JsonFileFactory
from models.Customer import Customer
from ui.SigninEx import SignInEx
from ui.SignUp import Ui_MainWindow

class SignUpEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Kết nối sự kiện cho các nút
        self.pushButtonSignUp.clicked.connect(self.save_user)  # Nút "SIGN UP"
        self.pushButtonSignIn.clicked.connect(self.switch_to_signin)  # Nút "Sign In Now!!!"

        # Khởi tạo JsonFileFactory để quản lý dữ liệu người dùng
        self.jff = JsonFileFactory()
        self.customer_file = "../database/Customers.json"

    def show_message(self, title, text):
        """Hiển thị hộp thoại cảnh báo"""
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setStyleSheet("QLabel{ color: black; } QWidget{ background-color: white; }")
        msg.exec()

    def save_user(self):
        email = self.lineEditGmail.text().strip()
        username = self.lineEditUsername.text().strip()
        password = self.lineEditPw.text().strip()
        confirm_password = self.lineEditRePw.text().strip()
        is_agreed = self.radioButtonAgree.isChecked()  # Kiểm tra checkbox đồng ý

        # Kiểm tra nếu chưa đồng ý với điều khoản
        if not is_agreed:
            self.show_message("Lỗi", "Bạn phải đồng ý với điều khoản để tiếp tục đăng ký!")
            return

        # Kiểm tra nhập đầy đủ thông tin
        if not email or not username or not password or not confirm_password:
            self.show_message("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        # Kiểm tra mật khẩu nhập lại
        if password != confirm_password:
            self.show_message("Lỗi", "Mật khẩu xác nhận không khớp!")
            return

        # Đọc dữ liệu khách hàng hiện có từ file JSON
        customers = []
        if os.path.exists(self.customer_file):
            try:
                customers = self.jff.read_data(self.customer_file, Customer) or []
                customers = [Customer(**cus) if isinstance(cus, dict) else cus for cus in customers]
            except json.JSONDecodeError as e:
                self.show_message("Lỗi JSON", f"File JSON bị lỗi định dạng: {str(e)}")
                return
            except Exception as e:
                self.show_message("Lỗi", f"Lỗi khi đọc dữ liệu: {str(e)}")
                return

        # Kiểm tra email đã tồn tại chưa
        if any(user.email == email for user in customers):
            self.show_message("Lỗi", "Email đã được đăng ký!")
            return

        # Lưu tài khoản mới
        new_customer = Customer(email=email, username=username, password=password)  # Sử dụng Customer object
        customers.append(vars(new_customer))  # Chuyển thành dict trước khi lưu

        # Ghi dữ liệu xuống file JSON
        try:
            self.jff.write_data(customers, self.customer_file)
        except Exception as e:
            self.show_message("Lỗi", f"Lỗi khi lưu dữ liệu: {str(e)}")
            return

        # Hiển thị thông báo đăng ký thành công
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setWindowTitle("Thành công")
        msg.setText("Đăng nhập thành công!")
        msg.setStyleSheet("QLabel{ color: black; } QWidget{ background-color: white; }")
        msg.exec()

        # Chuyển về màn hình đăng nhập
        self.switch_to_signin()

    def switch_to_signin(self, event=None):
        """Chuyển sang màn hình đăng nhập"""
        self.login_window = SignInEx()
        self.login_window.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    signup_window = SignUpEx()
    signup_window.show()
    sys.exit(app.exec())
