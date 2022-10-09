import operator

from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
class Scrap:
    def __init__(self,url):
        html = urlopen(url)
        self.soup = BeautifulSoup(html, 'html.parser')
        self.table = self.soup.find('table', class_='wikitable sortable')
        self.counrty=[]
        self.Co2=[]

#html=urlopen('https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions')



    def gettr(self):
        trs=self.table.find_all('tr')

        for tr in trs:
            tds = tr.find_all('td')
            if len(tds) == 0:
                continue
            else:
                self.counrty.append(tds[0].text.strip())
                self.Co2.append(float(tds[4].text.strip('%')))


    def listProcess(self):
        dict2={}
        del self.counrty[0:3]
        del self.Co2[0:3]
        dict2=dict(zip(self.counrty,self.Co2))
        dict2=dict(sorted(dict2.items(), key=operator.itemgetter(1),reverse=True))
        return dict2











'''
p= Scrap('https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions')
p.gettr()
a=p.listProcess()
print(a)
'''






        




        



