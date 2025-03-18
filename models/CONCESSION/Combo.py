class Combo:
    def __init__(self, Name, Price):
        self.Name = Name
        self.Price = Price

    def __str__(self):
        """Trả về chuỗi mô tả combo"""
        return f"Combo: {self.Name} - Price: {self.Price} VND"
