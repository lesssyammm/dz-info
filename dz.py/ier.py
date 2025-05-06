from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    k = 0
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            k += 1
    if sqrt(n) == int(sqrt(n)):
        k += 1
    if k == 2:
        return True
    return False
    

def p(x):
    if x <= 2:
        return 2
    i = 1
    if x % 2 == 1:
        i = 0
    while i >= 0:
        if is_prime(x - i) == True:
            return x - i
        if is_prime(x + i) == True:
            return x + i
        i += 2
        

    
def f(n):
    if n == 1:
        x = int(input())
        return p(x)
    if n == 2:
        dig = float(input())
        c = int(dig)
        b = dig - c
        return b
    if n == 0:
        return
    
    
while 1:
    print("[0] - завершение", "[1] - ближ. простое число", "[2] - действительная часть", sep = '\n')
    n = int(input("> "))
    if n == 0:
        break
    print(f(n))