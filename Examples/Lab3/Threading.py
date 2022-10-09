from Database import Database

import threading

class Threading():
    def __init__(self):
        self.I=Database()

        self.threadLock = threading.Lock()
        self.list=[]


    def Fetch(self,i):
        self.threadLock.acquire()
        data=self.I.fetchdata(i)
        self.list.append(data)
        self.threadLock.release()



    def Threadlist(self):
        threadlist=[]
        for index in range(1,7):
            thread = threading.Thread(target=self.Fetch, args=(index,))
            print("inserting Thread " + thread.name)
            threadlist.append(thread)

        for index in range(len(threadlist)):
            print("starting Thread " + threadlist[index].name)
            threadlist[index].start()

        for index in range(len(threadlist)):
            print("joining Thread " + threadlist[index].name)
            threadlist[index].join()







