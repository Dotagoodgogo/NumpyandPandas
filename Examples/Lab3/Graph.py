import pylab as p

from matplotlib import pyplot as plt

from Threading import Threading
from Database import Database

import numpy as np


class Graph:
    def __init__(self):
        self.I = Database()
        self.G = Threading()

    def Linear(self,i):
        plt.xlabel("Year")
        plt.ylabel("data")
        plt.title(" Global Radiative Forcing, CO2-equivalent mixing ratio, and the AGGI 1979-2018")
        year_x = self.I.fetchyear()
        data_y = self.G.list[i]

        coef = np.polyfit(year_x, data_y, 1)
        poly1d_fn = np.poly1d(coef)

        plt.plot(year_x, data_y, 'yo', year_x, poly1d_fn(year_x), '--k')
        plt.show()


    def Plot(self):
        self.G.Threadlist()
        for i in range(len(self.G.list)):
            self.Linear(i)

A=Graph()
A.Plot()
#The graph is shown one by one.






