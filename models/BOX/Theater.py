class Theater:
    def __init__(self,ThId, location):
        self.ThId = ThId
        self.location = location
    def __str__(self):
        return f"{self.ThId}\t{self.location})"