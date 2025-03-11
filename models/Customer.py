class Customer:
    def __init__(self, CId, CName , Phone, Mail, DOB):
        self.CId=CId
        self.CName = CName
        self.Phone=Phone
        self.Mail=Mail
        self.DOB=DOB

    def __str__(self):
        return f"{self.CName}\t{self.Phone}\t{self.Mail}"