from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

class Scrap:
    def __init__(self):
        self.list=[]
        url ="https://gml.noaa.gov/aggi/aggi.html"
        html = urlopen(url)
        self.soup = BeautifulSoup(html, 'html.parser')

    def scrap(self):
        table = self.soup.find('table', class_='table table-bordered table-condensed table-striped table-header')
        tbody=table.find('tbody')
        trs=tbody.find_all('tr')

        for tr in trs:
            tds=tr.find_all('td')[0:7]
            self.list.append(tds)

        return self.list



p=Scrap()
print(p.scrap())


