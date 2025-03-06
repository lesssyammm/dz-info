#кол-во делителей
from math import sqrt

def f(n):
    t = 0
    d = 1
    while d < sqrt(n):
        if n % d == 0:
            t += 1
        d += 1
    if sqrt(n) == int(sqrt(n)):
        t += 1
    return t


n = int(input())
x = f(n)
print(x)
