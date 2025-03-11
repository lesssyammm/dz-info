from random import randint
n = 10
a = [randint(-100, 100) for _ in range(n)]


#7
a = [1, 4, 5, 10, 20, 25, 100, 200, 233, 230, 201, 44, 13, 8, 2]
a.sort()
print(a)
print(a[-1])

#8

a.sort(reverse = True)
print(a)
x = int(input())
L = 0
R = n
while R - L != 1:
    c = (R + L) // 2
    if x > a[c]:
        R = c
    else:
        L = c
        
print(a[L + 1], a[L - 1])