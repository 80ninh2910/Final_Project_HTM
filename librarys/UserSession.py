
from librarys.DataConnector import DataConnector


class UserSession:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.username = ""
            cls._instance.email = ""
        return cls._instance

    def set_user(self, input):
        info=self.get_info(input)
        if info:
            self.email=info["email"]
            self.username=info["username"]


    def get_user(self):
        return {"username": self.username, "email": self.email}

    def clear(self):
        self.username=""
        self.email=""

    def get_info(self,input):
        dc=DataConnector()
        for c in dc.cus:
            if c.email==input or c.username==input:
                return {"username":c.username,"email":c.email}