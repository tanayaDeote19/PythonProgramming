import threading
import time

def funtion(seconds):
    print(f"Sleeping for {seconds}")
    time.sleep(seconds)

#by Calling function
time1 = time.perf_counter()
funtion(4)
funtion(2)
funtion(3)
time2 = time.perf_counter()-time1
print(time2)

#using Multithreading
time1 = time.perf_counter()
t1 = threading.Thread(target=funtion,args=[4])
t2 = threading.Thread(target=funtion,args=[2])
t3 = threading.Thread(target=funtion,args=[3])
t1.start()
t2.start()
t3.start()
time2 = time.perf_counter()-time1
print(time2)



