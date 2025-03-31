d = {}
for i in range(int(input())):
    f, *op = input().split()
    d[f] = op
a = []
for j in range(int(input())):
    s, f = input().split()
    op = s[0].upper()
    a.append(op)
    for key, val in d.items():
        if a[j] in val:
            print("OK")
        else:
            print("Access denied")


