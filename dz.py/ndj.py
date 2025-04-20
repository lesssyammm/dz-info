a = {}
for i in range(0, 1000):
    a[i] = i * i
v = a.values()
k = a.keys()
v = list(v)
k = list(k)
ind = -1
target = 1369
for x in range(len(v)):
    if v[x] == target:
        ind = x
if ind == -1:
    print("NO")
else:
    print(k[ind])