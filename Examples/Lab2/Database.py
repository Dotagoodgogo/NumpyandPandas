import sqlite3
from Scrap import Scrap



class Database:
    def __init__(self, url):
        self.I = Scrap(url)
        self.I.gettr()
        self.dict=self.I.listProcess()
        self.table=[]
        self.TopCountry=[]
        self.Topdata=[]


    def CreateTable(self):
        conn = sqlite3.connect("Co2.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE Co2(
        Country TEXT,
        Med REAL
        )""")
        conn.commit()

        conn.close()

    def insert(self):

        co2=list(self.dict.values())
        country=list(self.dict.keys())
        conn = sqlite3.connect("Co2.db")
        c = conn.cursor()
    
        for i in range(len(self.I.Co2)):
            c.execute(""" INSERT INTO Co2 (Country,Med) VALUES (?, ?)""",(country[i],co2[i]))
    
        conn.commit()
        conn.close()


    def fetch(self):
        conn = sqlite3.connect("Co2.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Co2")
        self.table=c.fetchall()
        print(self.table)
        conn.commit()
        conn.close()

    def fetchTop10(self):
        conn = sqlite3.connect("Co2.db")
        conn.row_factory = lambda cursor, row: row[0]
        c = conn.cursor()
        c.execute("SELECT Country FROM Co2 LIMIT 10")
        self.TopCountry=c.fetchall()
        c.execute("SELECT Med FROM Co2 LIMIT 10")
        self.Topdata=c.fetchall()

        conn.commit()
        conn.close()



























