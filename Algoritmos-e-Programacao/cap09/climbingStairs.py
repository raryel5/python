import time

def climb(n, memo:dict={}):
    if n in memo:
        return memo[n]

    if n == 0:
        return 1
    if  n == -1: 
        return 0
    
    memo[n] = climb(n-1) + climb(n-2)

    return memo[n]

startTime = time.time()

print(climb(12))
print(time.time()-startTime)