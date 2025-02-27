#простое число
from math import sqrt
def f(n):
    k = 0
    for d in range(1, int(sqrt(n)) + 1):
            if n % d == 0:
                  k += 1
    if k == 1:
          return True
    else:
          return False

n = 1247417
x = f(n)
print(x)
