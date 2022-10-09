import re


class AnnualTemperature():
    def __init__(self,file):
        self.file=file


    def Annual_method(self):                #open the file and put into dictionary
        file2 = open(self.file, "r")
        text = file2.readlines()
        year = []
        temp = []
        dict2 = {}
        del text[0:5]

        for element in text:
            data = re.search("<TBODY><TR><TD>(\d+)</TD><TD>((\d+.\d+)|(.\d+.\d+))", element)
            if data != None:
                year.append(int(data.group(1)))
                temp.append(round(float(data.group(2)),3))

        dict2 = dict(zip(year, temp))
        file2.close()

        return dict2





