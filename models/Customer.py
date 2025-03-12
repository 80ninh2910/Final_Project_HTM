class Customer:
    def __init__(self,CId, email, username, password):
        self.CId=CId
        self.email=email
        self.username=username
        self.password=password
    def __str__(self):
        return f"{self.CId}\t{self.email}\t{self.username}\t{self.password}"