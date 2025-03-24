class Customer:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def __str__(self):
        return f"Customer: {self.username} - Email: {self.email}"


