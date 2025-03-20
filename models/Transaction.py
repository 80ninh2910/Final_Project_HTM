from datetime import datetime

class Transaction:
    def __init__(self, theater, showtime, seats, num_tickets, order_items,user_name,mail,price):
        self.transaction_id = self.generate_transaction_id()
        self.theater = theater
        self.showtime = showtime
        self.seats = seats
        self.num_tickets = num_tickets
        self.order_items = order_items
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.user_name = user_name
        self.mail = mail
        self.price = price
    @staticmethod
    def generate_transaction_id():
        """Tạo mã giao dịch duy nhất dựa trên thời gian."""
        return f"TXN-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    def __str__(self):
        return (f"Giao dịch User_name:{self.user_name} Mail:{self.mail} {self.transaction_id} - Rạp: {self.theater}, Suất: {self.showtime}, "
                f"Ghế: {self.seats}, Vé: {self.num_tickets}"
                f"tiền: {self.price}")
    def to_dict(self):
        """Chuyển đổi đối tượng thành dictionary để lưu vào JSON."""
        return {
            "transaction_id": self.transaction_id,
            "timestamp": self.timestamp,
            "user_name": self.user_name,
            "mail": self.mail,
            "theater": self.theater,
            "showtime": self.showtime,
            "seats": self.seats,
            "num_tickets": self.num_tickets,
            "order_items": self.order_items,
            "price": self.price

        }
