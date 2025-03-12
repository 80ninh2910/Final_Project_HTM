class Movie:
    def __init__(self,Mname,MType,dur,des):
        self.MTitle=Mname
        self.MType=MType
        self.dur=dur
        self.des=des
    def __str__(self):
        return f"{self.MTitle}\n{self.MType}\n{self.dur}\n{self.des}"
