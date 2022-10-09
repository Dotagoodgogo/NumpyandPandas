import multiprocessing
import threading
import time


def f(i):
    for p in range(3):

        time.sleep(i + 1)
        print('Thread #', i, "\n")
        #time.sleep(i)
    return


if __name__ == '__main__':
    process=[]
    start = time.perf_counter()
    for i in range(3):
        t = multiprocessing.Process(target=f, args=(i,))
        t.start()
        process.append(t)

    for t in process:
        t.join()

    finish= time.perf_counter()
    print("Finished in",round(finish-start,2),'seconds')
    
