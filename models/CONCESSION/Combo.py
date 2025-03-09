class Combo:
    def __init__(self, CbName,  CbPrice):
        self.CbName=CbName

        self.CbPrice = CbPrice

    def __str__(self):
        return f"{self.CbName}\t{self.CbPrice}"