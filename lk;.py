from math import *

def is_prime(p):
    k = 0
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            k += 2
    if sqrt(p) == int(sqrt(p)):
        k += 1
    if k == 0:
        return 1
    return 0


n = int(input())
p = 1
q = 1
for i in range(2, n):
    if n % i == 0 and is_prime(i) == 1:
        p = i
a = n // p
if is_prime(a) == 1:
    q = a
print(p, q)
        
