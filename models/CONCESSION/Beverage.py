from numpy.f2py.symbolic import number_types


class Beverage:
    def __init__(self, Name, Price):
        self.Name=Name

        self.Price=Price
    def __str__(self):
        return f"{self.Name}\t{self.Price}"