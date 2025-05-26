# s = []
# for i in range(-1, 999 + 1):
#     for j in range(0, 10):
#         sm = 1 + 7 + 2 + 3 + 9 + j
#         if i != -1:
#             for k in str(i):
#                 sm += int(k)
#         a = sm // 11
#         if sm % 11 == 0:
#             print(f"17{i}023{j}9", a)

#1+

# def x(dig):
#     k = 0
#     a = []
#     for i in range(2, int(dig**0.5) + 1):
#         if dig % i == 0 and prime(i) == 1:
#             k += 1
#             a.append(i)
#             if prime(dig//i) == 1:
#                 k += 1
#                 a.append(i)
#     if dig**0.5 == int(dig**0.5):
#         k += 1
#     if k > 4:
#         return a[-1]


# def prime(n):
#     c = 0
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             c += 2
#     if n**0.5 == int(n**0.5):
#         c += 1
#     if c == 0:
#         return 1
#     return 0


# def p(dig):
#     k = 0
#     a = []
#     for i in range(2, int(dig**0.5) + 1):
#         if dig % i == 0 and prime(i) == 1:
#             k += 1
#             if prime(dig//i) == 1:
#                 k += 1
#     if dig**0.5 == int(dig**0.5):
#         k += 1
#     if k > 4:
#         return 1
#     return 0



# for i in range(0, 10):
#     for j in range(-1, 99 + 1):
#         if j == -1:
#             dig = int(f"34{i}89")
#         else:
#             dig = int(f"34{i}8{j}9")
#         if p(dig) == 1:
#             print(dig, x(dig))

#2++

def sm(n):
    k = 0
    d = 1
    while d < n ** 0.5:
        if n % d == 0:
            k += d
            k += n // d
        d += 1
    if n ** 0.5 == int(n** 0.5):
        k += int(n ** 0.5)
    return k

for i in range(0, 9999):
    for j in range(10):
        sd = int(f"7{j}")
        if i != 0:
            sd = int(f"{i}7{j}")
        for n in range(500_000, 600_000):
            if sm(n) == sd:
                print(n, sm(n))

        
#3

def count_del(n):
    k = 0
    d = 4
    while d < n ** 0.5:
        if n % d == 0 and str(d)[0] == "4":
            k += 2
        d += 1
    if n ** 0.5 == int(n ** 0.5):
        k += 1
    if k == 24:
        return 1
    return 0


        
for n in range(1, 10 ** 6):
    if count_del(n) == 1:
        print(n)

#4+
# def f(n):
#     k = 0
#     for i in range(1, 9):
#         a = int(f"{i}4")
#         if n % a == 0:
#             k += 1
#     return k

# for i in range(-1, 9999 + 1):
#     for j in range(10):
#         n = int(f"128{j}64")
#         if i != -1:
#             n = int(f"1{i}28{j}64")
#         if n % 124 == 0 and f(n) == 5:
#             print(n, n // 124)
        
    

#5

# def prime(n):
#     c = 0
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             c += 2
#     if n**0.5 == int(n**0.5):
#         c += 1
#     if c == 0:
#         return 1
#     return 0

# def del_(n):
#     d = 1
#     a = []
#     while d < n ** 0.5:
#         if n % d == 0 and prime(d) == 1:
#             a.append(d)
#             a.append(n // d)
#         d += 1
#     if n ** 0.5 == int(n ** 0.5):
#         a.append(n ** 0.5)
#     return a
# prime(del_(213))
    
# for n in range(33333, 55555):
#     if n % del_(n) == 0 and del_(n) > 250:
#         print(n // del_(n), del_(n))

#6

# def f(n):
#     a = []
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             a.append(i)
#             a.append(n // i)
#     if n ** 0.5 == int(n ** 0.5):
#         a.append(int(n ** 0.5))
#     return a

# for n in range(106732567, 152673836):
#     if len(f(n)) == 3:
#         print(n, f(n)[-2])

#7+

# def m(k):
#     a = []
#     for i in range(2, k):
#         if k % i == 0:
#             a.append(i)
#             a.append(k // i)
#             break
#     if len(a) == 0:
#         return 0
#     return a[0] + a[1]


# for i in range(-1, 99+1):
#     for j in range(10):
#         if i == -1:
#             k = int(f"512{j}34")
#         else:
#             k = int(f"51{i}2{j}34")
#         if m(k) != 0 and m(k) % 117 == 0:
#             print(k, m(k))
