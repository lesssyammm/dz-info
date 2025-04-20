from math import sqrt

    
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


a = [] #список простых чисел
def g(n):
    k = 0
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            k += 1
    if k == 0:
        return True
    return False




for i in range(2, 1000):#формируем список простых
    if g(i) == True:
        a.append(i)

def p(x):#поиск ближ простого
    for j in range(len(a)):
        q = x - a[j]
        w = a[j + 1] - x
        if q < w:
            return a[j]
        if q == w:
            return a[j]

print("[0] - завершение", "[1] - ближ. простое число", "[2] - действительная часть", sep = '\n')

n = int(input())
print(f(n))