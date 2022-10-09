import re


class CarbonEmmission:
    def __init__(self,file):
        self.file=file


    def carbon_method(self):                            #read the file and print the dictionary

        file2=open(self.file,"r")
        text = file2.readlines()
        Co = 0
        year = []
        del text[0:4]
        yearlyCo = []
        yearlyCo2 = []

        for element in text:
            niu = re.search("<TD>(\d+)</TD><TD>\d+</TD><TD>\d+.\d+</TD><TD>(\d+.\d+)</TD><TD>\d+.\d+</TD><TD>\d+.\d+</TD>",
                            element)

            if niu != None:
                year.append(int(niu.group(1)))
                yearlyCo.append(float(niu.group(2)))

        year = set(year)
        while len(yearlyCo) != 0:
            if len(yearlyCo) < 12:
                Co = round(sum(yearlyCo)/11, 2)
                del yearlyCo[0:11]
            else:
                for i in range(0,12):
                    Co = yearlyCo[i] + Co
                del yearlyCo[0:12]
            yearlyCo2.append(round(Co/12, 2))
            Co = 0
        dict1 = dict(zip(year, yearlyCo2))
        file2.close()
        return dict1


