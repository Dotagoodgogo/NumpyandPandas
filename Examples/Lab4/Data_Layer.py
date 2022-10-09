import xml.etree.ElementTree as ET
import sqlite3
import json
from User_Layer import User
class Database:
    def __init__(self):
        #self.I=User()
        self.tree = ET.parse('UNData.xml')
        self.root = self.tree.getroot()
        self.Country=[]
        self.Year=[]
        self.Value=[]


    def dataxml(self):
        data=self.root.find('data')
        for element in data.findall('record'):
            Country=element.find('Country').text
            Year = element.find('Year').text
            Value = element.find('Value').text
            self.Country.append(Country)
            self.Year.append(Year)
            self.Value.append(Value)

    def CreateTable(self):
        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE Data(
        Country TEXT,
        Year INTEGER,
        Value Real
        )""")
        conn.commit()

        conn.close()

    def Insert(self):

        conn = sqlite3.connect("Data.db")
        c = conn.cursor()

        for i in range(len(self.Country)):
            c.execute(""" INSERT INTO Data
             (Country,Year,Value) VALUES (?, ?,?)""", (self.Country[i], self.Year[i],self.Value[i]))

        conn.commit()
        conn.close()

    def Fetch(self):
        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Co2")
        self.table = c.fetchall()
        print(self.table)
        conn.commit()
        conn.close()

    def Delete(self):
        conn=sqlite3.connect("Data.db")
        c=conn.cursor()
        c.execute("DELETE FROM Data")
        conn.commit()
        conn.close()

    def FetchbyCountry(self,Country):

        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Data WHERE Country=?", (Country,))
        Data = c.fetchall()
        conn.commit()
        conn.close()

        if len(Data)==0:
            print("No such country in the list.")
        else:
            JsonCountry=json.dumps(Data)

            return JsonCountry








    def FetchbyYear(self,Year):
        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Data WHERE Year=?", (Year,))
        Data = c.fetchall()
        conn.commit()
        conn.close()

        if len(Data)==0:
            print("No such year in the list.")
        else:
            self.Jsonyear=json.dumps(Data)
            return self.Jsonyear











