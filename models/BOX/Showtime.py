class Showtime:
    def __init__(self, SId, Movie, Theater, time, seats):
        self.SId = SId
        self.time = time
        self.seats = seats
        self.Movie=Movie
        self.Theater=Theater

    def __str__(self):
        return f"{self.Movie}\t{self.Theater}\t{self.time}\t{self.seats}"

