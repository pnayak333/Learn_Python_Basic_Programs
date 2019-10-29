#Store value in the cache and then return the value
# Built in function - [from functtools import lru_cache ]
#[@Lru_cache(maxsize = 1000)
cache = {}

def Fibonacci(n):
    #if we cache the value then retun it
    if type(n) != int:
        raise TypeError("Enter the Interger NUmber")
    if n < 1:
        raise TypeError("Enter the Positive Interger")
    if n in cache:
        return cache[n]
    if n ==0 :
        value = 0
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = Fibonacci(n-1) + Fibonacci(n-2)

    cache[n] = value
    return value
for n in range(1,100):
    print(n, "FIB :", Fibonacci(n))
