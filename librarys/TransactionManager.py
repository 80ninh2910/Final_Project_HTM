import json
import os

from PyQt6.uic.Compiler.qtproxies import QtWidgets


class TransactionManager:
    def __init__(self):
        self.history_file = "../database/history_transaction.json"

    def show_message(self, title, text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setStyleSheet("QLabel{ color: black; } QWidget{ background-color: white; }")
        msg.exec()

    def save_transaction(self, transaction_data):
        # Kiểm tra nếu file tồn tại và có dữ liệu JSON hợp lệ
        if os.path.exists(self.history_file) and os.path.getsize(self.history_file) > 0:
            try:
                with open(self.history_file, "r", encoding="utf-8") as f:
                    transactions = json.load(f)  # Đọc danh sách cũ
            except json.JSONDecodeError:
                transactions = []  # Nếu file lỗi, đặt lại danh sách rỗng
        else:
            transactions = []

        # Thêm giao dịch mới vào danh sách
        transactions.append(transaction_data)

        # Ghi lại file JSON hợp lệ
        with open(self.history_file, "w", encoding="utf-8") as f:
            json.dump(transactions, f, indent=4, ensure_ascii=False)

