# def f(ost):
#     r = ''
#     if ost == 0.0:
#         return '0'
#     while ost > 0:
#         ost *= 2
#         c = int(ost)
#         r += str(c)
#         ost -= c
#     return r

# n = float(input())
# zn = '0'
# if n < 0:
#     zn = '1'
# n = abs(n)
# c = int(n)
# ost = n - c
# c = bin(c)[2:]
# p = len(c) - 1 + 127
# p = bin(p)[2:]
# r = zn + p + c[1:] + f(ost)
# r = r + '0'*(32 - len(r))
#print(hex(int(r, 2))[2:].upper())

#2


a = input()
if a[0] not in 'ABCDEF':
    a = int(a, 16)
    a = bin(a)[2:]#10000111 11000100 101000000000000
    p = a[0:8]#'10000111'
    p = int(p, 2) #135
    p -= 127 #8
    c = a[8:8+p]#11000100
    dr = a[8+p:]#101000000000000
    r = '1' + c
    r = int(r, 2) #452
    s = 0
    for x in range(len(dr)):
        if dr[x] == '1':
            el = -(x) - 1
            d = 2 ** el
            s += d
    print(r + s)
else:
    a = int(a, 16)
    a = bin(a)[2:]
    p = a[1:9]
    p = int(p, 2)
    p -= 127
    c = a[9:9+p]
    dr = a[9+p:]
    r = '1' + c
    r = -int(r, 2)
    s = 0
    for x in range(len(dr)):
        if dr[x] == '1':
            el = -(x) - 1
            d = 2 ** el
            s += d
    print(r - s)