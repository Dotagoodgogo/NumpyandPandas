from Scrap import Scrap
import sqlite3


class Database:
    def __init__(self):
        self.I = Scrap()
        self.list=self.I.scrap()
        self.year=[]
        self.datalist=[]
        self.year=[]


    def CreateTable(self):
        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE Data(
        Year TEXT,
        CO2 TEXT,
        CH4 TEXT,
        N20 TEXT,
        CFC12 TEXT,
        CFC11 TEXT,
        TOTAL TEXT
        )""")
        conn.commit()

        conn.close()

    def insert(self):
        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        for i in range(len(self.list)):
            c.execute(""" INSERT INTO Data (Year,CO2,CH4,N20,CFC12,CFC11,TOTAL) VALUES (?,?,?,?,?,?,?)""",
                  (self.list[i][0].text,self.list[i][1].text,self.list[i][2].text,self.list[i][3].text
                   ,self.list[i][4].text,self.list[i][5].text,self.list[i][6].text))

        conn.commit()
        conn.close()

    def fetchdata(self,i):
        data=[]
        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Data")
        All=c.fetchall()
        for x in range(len(All)):
            data.append(float(All[x][i]))

        self.datalist=data
        data=[]
        conn.commit()
        conn.close()
        return self.datalist



    def fetchyear(self):
        year=[]
        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        c.execute("SELECT Year FROM Data")
        All = c.fetchall()
        for x in range(len(All)):
            year.append(float(All[x][0]))
        self.year=year
        year=[]
        conn.commit()
        conn.close()

        return self.year





