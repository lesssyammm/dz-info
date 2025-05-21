from random import randint


#8

n = 5
m = 5
a = [[randint(1, 9) for j in range(m)] for i in range(n)]
for x in a:
    print(*x)
b = [a[i][i] for i in range(n)]
print(max(b))

#9

mx = -100
for i in range(n):
    for j in range(m):
        if a[i][j] >= mx:
            mx = a[i][j]
print(mx)

#10

mn = 100
for i in range(n):
    for j in range(m):
        if a[i][j] <= mn and a[i][j] % 2 == 0 and a[i][j] > 0:
            mn = a[i][j]
if mn == 100:
    print("Не нашлось")
else:
    print(mn)

#11

p = []
for x in a:
    p.append(sum(x))
    print(sum(x), end=" ")
print()
smx = max(p)
print(smx)

#12

p = []
for x in a:
    p.append(sum(x))
    print(sum(x), end=" ")
print()
smn = min(p)
print(smn)
