class Popcorn:
    def __init__(self, Name, Price):
        self.Name = Name
        self.Price = Price

    def __str__(self):
        """Trả về chuỗi mô tả bắp rang"""
        return f"Popcorn: {self.Name} - Price: {self.Price} VND"
