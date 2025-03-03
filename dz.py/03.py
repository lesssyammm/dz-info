#1
from random import randint
n = 10
a = [randint(10, 200) for i in range(n)]
print(a)

for i in range(n - 1):
    for j in range(n - 1 - i):
        t1 = a[j]
        sm1 = 0 
        while t1:
            k = t1 % 10
            sm1 += k
            t1 //= 10
        t2 = a[j + 1]
        sm2 = 0 
        while t2:
            k = t2 % 10
            sm2 += k
            t2 //= 10
        if sm1 > sm2:
            a[j], a[j + 1] = a[j + 1], a[j]
            
print(a) # [99, 128, 141, 25, 154, 91, 23, 133, 117, 129]
#          [23, 141, 25, 133, 117, 154, 91, 128, 129, 99]
#           5,  6,   7,  7,   9,   10,  10, 11,  12,  18

#2

from random import randint
n = 10
a = [randint(1, 99) for i in range(n)]
print(a)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] // 10 < a[j + 1] // 10:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)

#3
from time import time
t = time()
from random import randint
n = 5000
a = [randint(100, 1000) for i in range(n)]
for i in range(n - 1):
    el = a[i]    
    ind = i
    while a[ind - 1] > el and ind - 1 >= 0:
        a[ind] = a[ind - 1]        
        ind = ind - 1    
    a[ind] = el

print(time() - t)

for j in range(n - 1):
    mn = a[j]
    ind = j
    for i in range(j, n):
        if a[i] < mn:
            mn = a[i]
            ind = i
    a[j], a[ind] = a[ind], a[j]

print(time() - t) #2.87  4.8

#4

a = [26, 10, 13, 16, 23, 17, 24]
n = len(a)
for j in range(n - 1):
    mn = a[j]
    ind = j
    for i in range(j, n):
        if a[i] % 2 == 0 and a[i] < mn:
            mn = a[i]
            ind = i
    a[j], a[ind] = a[ind], a[j]
    
print(a) #[10, 16, 13, 24, 23, 17, 26]