from Database import Database
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
        elif self.I.getoption()==4:
            self.G.Pie()


            
p=Back_End('https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions')
p.menu()
p.execute()

















