import functools
import time
@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return n*5

print(fx(20))
print("Done with 20")
print(fx(10))
print("Done with 20")
print(fx(30))
print("Done with 20")

print(fx(20))
print("Done with 20")
print(fx(10))
print("Done with 20")
print(fx(30))
print("Done with 20")

print(fx(22))
print("Done with 22")


