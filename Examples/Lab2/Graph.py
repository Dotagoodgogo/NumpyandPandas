from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

from Database import Database
from Scrap import Scrap
import numpy as np

class Graph:
    def __init__(self,url):
        self.I=Database(url)
        self.I.fetchTop10()

    def XY_plot(self):
        plt.xlabel("Country")
        plt.ylabel("2017 Co2 median(%)")
        plt.title(" Top 10 countries by carbon dioxide emissions")

        year_x =self.I.TopCountry
        temp_y =self.I.Topdata
        plt.xticks(rotation=40)

        plt.plot(year_x,temp_y)

        plt.show()

    def Bar_plot(self):
        plt.xlabel("Country")
        plt.ylabel("2017 Co2 median(%)")
        plt.title(" Top 10 countries by carbon dioxide emissions")
        year_x = self.I.TopCountry
        temp_y = self.I.Topdata
        plt.xticks(rotation=40)


        plt.bar(year_x,temp_y)
        plt.show()

    def Linear(self):
        try:
            plt.xlabel("Country")
            plt.ylabel("2017 Co2 median(%)")
            plt.title(" Top 10 countries by carbon dioxide emissions")
            country_x = self.I.TopCountry
            co2_y = self.I.Topdata
            plt.xticks(rotation=40)

            coef = np.polyfit(country_x, co2_y, 1)
            poly1d_fn = np.poly1d(coef)

            plt.plot(country_x, co2_y, 'yo', country_x, poly1d_fn(country_x), '--k')
            plt.show()
        except ValueError:
            print("Data is not linearly. Not avaliable for lab2.")

    def Pie(self):
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('equal')
        country = self.I.TopCountry
        co2 = self.I.Topdata
        ax.pie(co2, labels=country, autopct='%1.2f%%')
        plt.show()















