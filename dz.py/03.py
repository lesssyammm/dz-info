from random import randint
n = 10
a = [randint(1, 20) for _ in range(n)]

def qSort(a):
    if len(a) <= 1:
        return a
    else:
        el = a[0]
        L = [x for x in a if x < el]
        C = [x for x in a if x == el]
        R = [x for x in a if x > el]
        return qSort(L) + C + qSort(R)
    
print(qSort(a))