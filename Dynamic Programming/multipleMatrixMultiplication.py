"""
The logic behind multiple matrix mutiplication is as given below

A = 10*30
B = 30*5
C = 5*60
ABC =  (AB)C   || A(BC)

ABC =  (AB)C 
    =  10*30*5 + 10*5*60 operations
    =  4500 operation
----OR----
ABC =  A(BC)
    =  30*5*60 + 10*30*60 operations
    =  27000 operation


So to get which combination will require minimum no of operation will be used
for finding the Matrix Multiplication values
"""


def MatMul(dim):
    for 

no =  int(input("Enter number of matrix: "))
a=[]
for _ in range(no):
    a.append([int(x) for x in input().split()])
dimension =  a[0]
for i in a[1:]:
    dimension.extend([i[0]])


