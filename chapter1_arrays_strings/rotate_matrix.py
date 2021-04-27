# Rotate an n*n matrix. Can you do it inplace?
# Solution:
# Note : solution was not hard to get but the implementation makes it harder. Also the copying of arrays cause problem in python

import numpy as np
def top(i, n, a):
    return a[i, i:n-1 - i]
def right(i, n, a):
    return a[i:n-1 - i , n-1 - i]
def bottom(i, n, a):
    return a[n-1 - i, i+1:n-i]
def left(i, n, a):
    return a[i+1:n - i, i]
n = int(input())
a = []
for i in range(n):
    x = [x for x in input().split()]
    a.append(x)
a = np.array(a)
print(a)
for i in range(0, n//2 + 1):
    t = top(i, n , a)
    r = right(i, n , a) 
    b = bottom(i, n, a) 
    l = left(i, n, a) 
    temp = t[:].copy()
    a[i, i:n-1-i] = l[::-1]
    a[i+1:n-i, i] = b 
    a[n-1-i, i+1:n-i] = r[::-1]
    a[i:n-1-i, n-1-i] = temp
    # for every row just 
print(a)
         

