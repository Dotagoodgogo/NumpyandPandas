from Database import Database
from CarbonEmmission import CarbonEmmission
from AnnualTemperature import AnnualTemperature


class process:
    def __init__(self,file,file2):
        self.C=CarbonEmmission(file)
        self.A=AnnualTemperature(file2)
        self.D = Database()



    def getdata(self):      #getdata from the dictionary
        condata = self.C.carbon_method()
        temdata = self.A.Annual_method()
        minimum = min([min(condata.keys()),min(temdata.keys())])
        maximum = max([max(condata.keys()),max(temdata.keys())])

        for i in range(minimum, maximum):
            if i in condata.keys() and temdata.keys():
                a = self.D.turple_data(i, condata[i], temdata[i])
        return a






