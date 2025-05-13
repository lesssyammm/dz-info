import sys
sys.setrecursionlimit(100000)
def f(n):
    if n == 41:
        return 41
    if n > 41 and n % 2 == 0:
        return f(n - 1) - n
    if n > 41 and n % 2 != 0:
        return n * f(n - 2)
print(f(9094) // f(9089))