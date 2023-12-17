import time

#using time.time()
def usingWhile():
    i=0
    while i<1000:
        print(i)
        i=i+1


def usingFor():
    for j in range(1000):
        print(j)

a=time.time()
usingWhile()
time1=time.time()-a

a=time.time()
usingFor()
time2=time.time()-a

print(time1)
print(time2)


# #using time.strftime()
# recenttime = time.strftime('%H:%M:%S')
# print(recenttime)



#time.sleep()
# print(4)
# time.sleep(2)
# print(6)