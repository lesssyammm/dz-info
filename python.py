#простое число
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    k = 0
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            k += 2
    if sqrt(n) == int(sqrt(n)):
        k += 1
    if k == 2:
        return True
    return False
n = 13
x = is_prime(n)
print(x)
