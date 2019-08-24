import time
n = int(input())
a = time.time()
lookup = [0]*n

def fib(n):
    if lookup[n-1] == 0:
        if n<=1:
            lookup[n-1] = n
        else:
            lookup[n-1] = fib(n-1) +fib(n-2)

    return lookup[n-1]

print(fib(n))
b = time.time()
print(b-a)
