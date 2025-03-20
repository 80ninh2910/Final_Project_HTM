class PointDiscount:
    def __init__(self, customer):
        """Khởi tạo với đối tượng khách hàng."""
        self.customer = customer  # Đối tượng Customer chứa điểm tích lũy

    def add_points(self, amount_spent):
        """Cộng thêm điểm cho khách hàng dựa trên số tiền đã chi tiêu."""
        points_earned = amount_spent // 10000
        self.customer.points += points_earned
        return points_earned

    def use_points(self, amount_spent):
        """Sử dụng điểm để giảm giá và trả về số tiền cuối cùng sau khi trừ điểm."""
        if self.customer.points == 0:
            return amount_spent  # Nếu không có điểm, trả lại số tiền gốc

        # Tính số tiền giảm giá tối đa dựa trên số điểm hiện có
        max_discount = self.customer.points * 100  # Giả sử 1 điểm = 100 VND

        # Trừ tiền thanh toán nhưng không để giá trị tiền dưới 0
        final_amount = max(0, amount_spent - max_discount)

        # Tính số điểm đã sử dụng
        points_used = (amount_spent - final_amount) // 100
        self.customer.points -= points_used  # Trừ số điểm đã dùng

        return final_amount


