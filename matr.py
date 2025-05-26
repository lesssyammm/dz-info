from random import randint


# #8

# n = 5
# m = 5
# a = [[randint(1, 9) for j in range(m)] for i in range(n)]
# for x in a:
#     print(*x)
# b = [a[i][i] for i in range(n)]
# print(max(b))

# #9

# mx = -100
# for i in range(n):
#     for j in range(m):
#         if a[i][j] >= mx:
#             mx = a[i][j]
# print(mx)

# #10

# mn = 100
# for i in range(n):
#     for j in range(m):
#         if a[i][j] <= mn and a[i][j] % 2 == 0 and a[i][j] > 0:
#             mn = a[i][j]
# if mn == 100:
#     print("Не нашлось")
# else:
#     print(mn)

# #11

# p = []
# for x in a:
#     p.append(sum(x))
#     print(sum(x), end=" ")
# print()
# smx = max(p)
# print(smx)

# #12

# p = []
# for x in a:
#     p.append(sum(x))
#     print(sum(x), end=" ")
# print()
# smn = min(p)
# print(smn)

16 a)
n = 7
m = 7
a = [[randint(2, 9) for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i + j) >= n - 1 and i != 0 and i != 6 and j != 0 and j != 6:
            a[i][j] = 0

for x in a:
    print(*x)

16 b)

n = 7
m = 7
a = [[randint(2, 9) for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i + j) <= n - 1 and i != 0 and i != 6 and j != 0 and j != 6:
            a[i][j] = 0

for x in a:
    print(*x)

16 v)

n = 7
m = 7
a = [[randint(2, 9) for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i + j) >= n - 4 and (i + j) <= n + 2:
            a[i][j] = 0

for x in a:
    print(*x)

17 a)

def f(n, m):
    a = []
    k = 1
    for i in range(n):
        s = []
        for j in range(m):
            s.append(k)
            k += 1
        a.append(s)
    return a

n = 3
m = 4
a = f(n, m)
for x in a:
    print(*x)

17 b)

def f(n, m):
    a = []
    for i in range(n):
        s = []
        k = 1 + i
        for j in range(m):
            s.append(k)
            k += 3
        a.append(s)
    return a
n = 3
m = 4
a = f(n, m)
for x in a:
    print(*x)

17 v)

def f(n, m):
    a = []
    for i in range(1, n + 1):
        s = []
        k = n*m - n + i
        for j in range(m):
            s.append(k)
            k -= 3
        a.append(s)
    return a
n = 3
m = 4
a = f(n, m)
for x in a:
    print(*x)

18 a)

def f(n, m):
    a = []
    for i in range(n):
        s = []
        k = 1 + i
        for j in range(m):
            s.append(k)
            k += 1
        a.append(s)
    return a

n = 3
m = 4
a = f(n, m)
for x in a:
    print(*x)

18 b)

def f(n, m):
    a = []
    
    for i in range(n):
        s = []
        k = 1 + n * 2 - n + i
        for j in range(m):
            s.append(k)
            k -= 1
        a.append(s)
    return a

n = 3
m = 4
a = f(n, m)
for x in a:
    print(*x)

18 v)

def f(n, m):
    a = []
    for i in range(n):
        s = []
        k = n * 2 - i
        for j in range(m):
            s.append(k)
            k -= 1
        a.append(s)
    return a

n = 3
m = 4
a = f(n, m)
for x in a:
    print(*x)
