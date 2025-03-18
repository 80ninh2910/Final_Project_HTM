class Showtime:
    def __init__(self, SId, Movie, Theater, time, seats):
        self.SId = SId
        self.Movie = Movie
        self.Theater = Theater
        self.time = time
        self.seats = seats

    def __str__(self):
        """Trả về chuỗi mô tả suất chiếu"""
        return (
            f"Showtime ID: {self.SId}\n"
            f"Movie: {self.Movie}\n"
            f"Theater: {self.Theater}\n"
            f"Time: {self.time}\n"
            f"Seats Available: {self.seats}"
        )
