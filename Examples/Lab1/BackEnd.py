from interface import interface
from Graph import Graph


class Back_End:
    def __init__(self,file):
        self.I = interface()
        self.G = Graph(file)


    def menu(self):
        self.I.options()


    def execute(self):
        if self.I.getoption()==1:
            self.G.XY_plot()
        elif self.I.getoption()==2:
            self.G.Bar_plot()
        elif self.I.getoption()==3:
            self.G.Linear()


            


p=Back_End("Temperature.html")
p.menu()
p.execute()















