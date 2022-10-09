from matplotlib import pyplot as plt
from AnnualTemperature import AnnualTemperature
import numpy as np

class Graph:
    def __init__(self,file):
        self.A=AnnualTemperature(file)
        plt.xlabel("Year")
        plt.ylabel("Average Difference")
        plt.title("Average temperature anomaly,Global(C)")

    def XY_plot(self):


        dict = self.A.Annual_method()
        year_x = list(dict.keys())
        temp_y = list(dict.values())

        plt.plot(year_x,temp_y)
        plt.show()

    def Bar_plot(self):
        dict = self.A.Annual_method()
        year_x = list(dict.keys())
        temp_y = list(dict.values())

        plt.bar(year_x,temp_y)
        plt.show()

    def Linear(self):
        dict = self.A.Annual_method()
        year_x = list(dict.keys())
        temp_y = list(dict.values())

        coef = np.polyfit(year_x, temp_y, 1)
        poly1d_fn = np.poly1d(coef)

        plt.plot(year_x, temp_y, 'yo', year_x, poly1d_fn(year_x), '--k')
        plt.show()














