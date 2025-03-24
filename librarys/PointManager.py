import json
import os




class PointManager:
    def __init__(self, file_path="../database/customer_points.json"):
        self.file_path = file_path
        self.points_data = self.load_points()

    def load_points(self):
        """Tải dữ liệu điểm từ file JSON"""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        return {}

    def save_points(self):
        """Lưu dữ liệu điểm vào file JSON"""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.points_data, file, indent=4, ensure_ascii=False)

    def get_points(self, username, email):
        """Lấy số điểm của khách hàng"""
        key = f"{username}|{email}"
        return self.points_data.get(key, 0)

    def add_points(self, username, email, final_payment):
        """Cộng điểm dựa trên tổng tiền thanh toán"""
        key = f"{username}|{email}"
        new_points = final_payment // 10000  # 1 điểm cho mỗi 10,000 VND
        self.points_data[key] = self.get_points(username, email) + new_points
        self.save_points()

    def use_points(self, username, email, points_to_use):
        """Trừ điểm và trả về số tiền được giảm"""
        key = f"{username}|{email}"
        current_points = self.get_points(username, email)
        if points_to_use > current_points:
            return 0  # Không đủ điểm để sử dụng

        discount_amount = points_to_use * 100  # 1 điểm = 100 VND
        self.points_data[key] = current_points - points_to_use
        self.save_points()
        return discount_amount
