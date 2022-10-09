from collections import namedtuple


class Database:
    def __init__(self):
        self.data = []




    def turple_data(self,year,carbon,temperature):          #create namedturple
        data=namedtuple("data","year,carbon,temperature")
        item=data(year,carbon,temperature)
        self.data.append(item)
        return self.data

