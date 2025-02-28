#1

from random import randint
a = []
n = 8
for i in range(n):
    a.append(randint(1, 100))

print(a)

for i in range(n//2 - 1):
    for j in range(n//2 - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

for l in range(n//2, n):
    for k in range(n//2, n - 1):
        if a[k] < a[k + 1]:
            a[k], a[k + 1] = a[k + 1], a[k]

print(a)

#2
from random import randint

a = []
n = 8
for i in range(n):
    a.append(randint(1, 100))

print(a)
k1, k2 = 0, 0
for i in range(n-1):
    for j in range(-1, -n+i, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
print(a)