# def f(n):
#     n = oct(n)[2:]
#     k = 0
#     for i in n:
#         k += int(i)
#     if k % 2 == 0:
#         k = oct(k)[2:]
#         n += k
#     else:
#         k = oct(k)[2:]
#         n = k + n
#     r = int(n, 8)
#     return r

# a = []
# for n in range(483, 1000):
#     a.append(f(n))
# print(min(a))

# 2

# def f(n):
#     qw = ""
#     while n:
#         a = n % 4
#         qw = str(a) + qw
#         n //= 4
#     k = 0
#     for i in qw:
#         k += int(i)
#     if k % 2 == 0:
#         qw += qw[:2]
#     else:
#         qw = qw + "2"
#         qw = "10" + qw[2:] 
#     r = int(qw, 4)
#     return r


# for n in range(4, 100):
#     if f(n) < 250:
#         print(n)

# 3


# from math import sqrt


# def is_prime(i):
#     c = 0
#     for j in range(2, int(sqrt(i)) + 1):
#         if i % j == 0:
#             c += 2
#     if sqrt(i) == int(sqrt(i)):
#         c += 1
#     if c == 0:
#         return 1
#     else:
#         return 0


# def f(n):
#     n = str(n)[::-1]
#     k = 0
#     for j in range(0, len(n), 2):
#         k += int(n[j])
#     K = k ** 2
#     L = 0
#     for i in n:
#         if is_prime(int(i)) == 1:
#             L += int(i) ** 2
#     r = abs(K - L)
#     return r


# def uniq(n):
#     n = str(n)
#     k = 0
#     for i in n:
#         a = n.count(i)
#         k += a
#     if k == len(n):
#         return 1
#     else:
#         return 0


# for n in range(999999, 99999, -1):
#     if uniq(n) == 1:
#         if f(n) == 407:
#             print(n)
#             break


# 4

# def f(n):
#     a = []
#     n = str(n)
#     for i in n:
#         a.append(i)
#     a = sorted(a)
#     sr = a[len(a) // 2]
#     r = sr + n + sr
#     c = 0
#     for j in r:
#         c += int(j)
#     r = int(r) / c
#     return r


# def uniq(n):
#     n = str(n)
#     k = 0
#     for i in n:
#         a = n.count(i)
#         k += a
#     if k == len(n):
#         return 1
#     else:
#         return 0


# k = 0
# for n in range(100, 1000):
#     if uniq(n) == 1:
#         if f(n) == int(f(n)):
#             k += 1
# print(k)

s = []
for i in range(-1, 999 + 1):
    for j in range(0, 10):
        sm = 1 + 7 + 2 + 3 + 9 + j
        if i != -1:
            for k in str(i):
                sm += int(k)
        a = sm // 11
        if sm % 11 == 0:
            print(f"17{i}023{j}9", a)
