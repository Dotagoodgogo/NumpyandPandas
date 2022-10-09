from User_Layer import User
from matplotlib import pyplot as plt
from Data_Layer import Database
import json
from User_Layer import User

class Business:
    def __init__(self):
        self.I = User()
        self.G = Database()
        self.Country=[]
        self.Year=[]
        self.Value=[]
        self.Cou=[]

    def DataCenter(self):
        self.I.Pull_down()
        A = self.G.FetchbyCountry(self.I.clicked.get())
        self.Cou = json.loads(A)
        self.Country = self.Cou[1][0]

    def DataProc(self):

        for i in range(len(self.Cou)):
            if self.Cou[i][1] in self.Year:
                break
            else:
                self.Year.append(self.Cou[i][1])
            self.Value.append(round(self.Cou[i][2], 2))

    def Value(self):
        return self.Value

    def Country(self):
        return self.Country

    def Year(self):
        return self.Year



'''
    def XY_plotbyY(self,year):
        A= self.G.FetchbyYear(year)
        Cou = json.loads(A)
        for i in range(len(Cou)):
            self.Country.append(Cou[i][0])
            self.Value.append(round(Cou[i][2],2))
        plt.xlabel("Country")
        plt.ylabel("Co2 emmision")
        plt.title(f" countries carbon dioxide emissions by{Cou[0][1]}year")
        plt.xticks(fontsize=7)
        plt.xticks(rotation=90)
        plt.plot(self.Country, self.Value)
        plt.show()


    def XY_plotbyC(self):
        A = self.G.FetchbyCountry()
        Cou = json.loads(A)
        for i in range(len(Cou)):
            if Cou[i][1] in self.Year:
                break
            else:
                self.Year.append(Cou[i][1])


            self.Value.append(round(Cou[i][2],2))
        plt.xlabel("Year")
        plt.ylabel("Co2 emmision")
        plt.title(f" {Cou[0][0]} carbon dioxide emissions in 25 Years")
        plt.xticks(fontsize=7)
        plt.xticks(rotation=90)
        plt.plot(self.Year, self.Value)
        plt.show()
'''




