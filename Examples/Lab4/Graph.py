from User_Layer import User
from matplotlib import pyplot as plt
from Data_Layer import Database

import json





class Graph:
    def __init__(self):
        self.Country=[]
        self.Year=[]
        self.Value=[]


    def DataProc(self,x):
        self.Country = x[1][0]

        for i in range(len(x)):
            if x[i][1] in self.Year:
                break
            else:
                self.Year.append(x[i][1])
            self.Value.append(round(x[i][2], 2))


    def XY_plotbyY(self):

        plt.xlabel("Country")
        plt.ylabel("Co2 emmision")
        plt.title(f" countries carbon dioxide emissions by{self.Country}year")
        plt.xticks(fontsize=7)

        plt.plot(self.Year, self.Value)

        plt.show()

    def XY_plotbyC(self):

        plt.xlabel("Year")
        plt.ylabel("Co2 emmision")
        plt.title(f" {self.Country} carbon dioxide emissions in 27 Years")
        plt.xticks(fontsize=7)

        plt.xticks(rotation=90)

        plt.plot(self.Year, self.Value)

        plt.show()


