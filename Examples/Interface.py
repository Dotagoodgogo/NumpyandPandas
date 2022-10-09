from Process import process
import Database
import cProfile
class interface:
    def __init__(self,file1,file2):                 #input data for namedturple
        self.p = process(file1,file2)

    def inputdata(self):                            #input namedturple
        data = self.p.getdata()
        return data

    def printdata(self,list):                       #print the data
        print("Year Carbon  Temperature")
        txt='{:.3f} {:.3f}'
        for i in range(len(list)):
            print(list[i].year, txt.format(list[i].carbon, list[i].temperature))






if __name__ == '__main__':
    p = interface("Co2.html", "Temperature.html")
    data = p.inputdata()
    p.printdata(data)
    cProfile.run('p.inputdata')
    cProfile.run('p.printdata(data)')


"""
126 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 Interface.py:12(printdata)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       61    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       60    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
       
       3 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""



