class Theater:
    def __init__(self, ThId, location):
        self.ThId = ThId
        self.location = location

    def __str__(self):
        """Trả về chuỗi mô tả rạp chiếu phim"""
        return f"Theater ID: {self.ThId} - Location: {self.location}"
