n = int(input())
import time
a = time.time()

def fib(n):
    lookup = [0]*n
    lookup[0]=0
    lookup[1]=1
    for i in range(2, n):
        lookup[i] = lookup[i-1]+lookup[i-2]
    return lookup[n-1]

print(fib(n))
b = time.time()
print(b-a)
