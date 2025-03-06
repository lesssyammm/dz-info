#Сортировка вставками
from random import randint

n = 15
a = [randint(1, 30) for _ in range(n)]
print(a)

print(sorted(a))

for i in range(1, n):
    el = a[i]
    ind = i
    while a[ind - 1] > el and ind - 1 >= 0:
        a[ind] = a[ind - 1]
        ind = ind - 1
    a[ind] = el

print(a)
