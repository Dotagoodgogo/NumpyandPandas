import sqlite3
from AnnualTemperature import AnnualTemperature
from matplotlib import pyplot as plt
import numpy as np


class Database:
    def __init__(self, file):
        self.table=[]
        self.A=AnnualTemperature(file)

        plt.xlabel("Year")
        plt.ylabel("Average Difference")
        plt.title("Average temperature anomaly,Global(C)")






    def CreateTable(self):
        conn = sqlite3.connect("Temperature.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE Temperature(
        Year INTEGER,
        Median_Tem REAL
        )""")
        conn.commit()

        conn.close()

    def insert(self,year,number):
        conn = sqlite3.connect("Temperature.db")
        c = conn.cursor()
        sqlite = """ INSERT INTO Temperature
                (Year,Median_Tem) VALUES (?, ?)"""
        data=(year,number)
        c.execute(sqlite,data)
        conn.commit()
        conn.close()

    def fetch(self):
        conn = sqlite3.connect("Temperature.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Temperature")
        self.table=c.fetchall()
        print(self.table)
        conn.commit()
        conn.close()

    def Delete(self):
        conn = sqlite3.connect("Temperature.db")
        c = conn.cursor()
        c.execute("DELETE from Temperature where Year=1999")

        conn.commit()
        conn.close()

    def grab(self):
        dict=self.A.Annual_method()
        return dict

    def fetchpart(self,minnumber,maxnumber):
        if minnumber<maxnumber:
            conn = sqlite3.connect("Temperature.db")
            c = conn.cursor()
            c.execute("SELECT * FROM Temperature Where Year BETWEEN ? AND ?",(minnumber,maxnumber))
            self.table=c.fetchall()
            print(self.table)
            conn.commit()
            conn.close()
        else:
            print("error in range.")

    def __getitem__(self,year):
        conn = sqlite3.connect("Temperature.db")
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM Temperature Where Year=?",(year,))
            data=c.fetchall()
            conn.commit()
            conn.close()
            return data[0][1]
        except IndexError:
            print("index out of range!")

    def getmedian(self):
        list=[]
        for i in range(len(self.table)):
            list.append(self.table[i][1])
        return list


    def iterator(self):
        for element in self.table:
            print(element)

    def sort(self):
        a=sorted(self.getmedian())
        return a

    def XY_plot(self):
        x=[]
        y=[]
        for i in range(len(self.table)):
            x.append(self.table[i][0])
            y.append(self.table[i][1])


        year_x= x
        temp_y = y

        plt.plot(year_x,temp_y)
        plt.show()



















