№1

n, m = map(int, input().split())
a = set()
b = set()
for i in range(n):
    a.add(int(input()))

for i in range(m):
    b.add(int(input()))
    
c = list(a & b)
c.sort()
d = list(a - b)
d.sort()
e = list(b - a)
e.sort()

print(len(c))
print(*c)
print(len(d))
print(*d)
print(len(e))
print(*e)

№2

a = int(input())
s = [input() for _ in range(a)]
s = " ".join(s)
s = s.split()
c = set(s)
    
print(len(c))

№3

n = int(input())
a = [i for i in range(1,n+1)]
s = set(a)
while True:
    k = input()
    if k == 'HELP':
        break
    nw = input()
    if nw == 'NO':
        s -= set(k.split())
    elif nw == 'YES':
        s &= set(k.split())

print(*s)