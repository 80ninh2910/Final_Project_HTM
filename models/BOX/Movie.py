class Movie:
    def __init__(self, MTitle, MType, dur, des):
        self.MTitle = MTitle
        self.MType = MType
        self.dur = dur
        self.des = des

    def __str__(self):
        """Trả về chuỗi mô tả phim"""
        return (
            f"Movie Title: {self.MTitle}\n"
            f"Type: {self.MType}\n"
            f"Duration: {self.dur}\n"
            f"Description: {self.des}"
        )