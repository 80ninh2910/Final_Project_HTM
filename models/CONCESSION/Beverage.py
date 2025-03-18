class Beverage:
    def __init__(self, Name, Price):
        self.Name = Name
        self.Price = Price

    def __str__(self):
        """Trả về chuỗi mô tả đồ uống"""
        return f"Beverage: {self.Name} - Price: {self.Price} VND"