import time

cache={}

def fibonacci(n):
    global cache
    if n in cache:
        return cache[n]

    if n==0:
        result=0
    elif n==1:
        result=1
    else:
        result=fibonacci(n-1)+fibonacci(n-2)
    cache[n]=result
    return result

for i in range(18,100,5):
    start=time.time()
    result=fibonacci(i)
    end=time.time()
    duration=end-start
    print(i,"   ", result,"   ",duration)




