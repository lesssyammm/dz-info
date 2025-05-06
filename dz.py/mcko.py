print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = w and (y == (z <= (x or y)))
                if f == True:
                    print(x, y, z, w)

# # s = 666 * '6'
# # while "666" in s or "111" in s:
# #     if "666" in s:
# #         s = s.replace("66", "1", 1)
# #     else:
# #         s = s.replace("111", "6", 1)
# # print(s)


# # s = []
# # for x in range(21):
# #     a = 8 * 21 ** 6 + 2 * 21 ** 5 + 9 * 21 ** 4 + 3 * 21 ** 3 + 4 * 21 ** 2 + x * 21 ** 1 + 2
# #     b = 2 * 21 ** 6 + 9 * 21 ** 5 + 2 * 21 ** 4 + 4 * 21 ** 3 + x * 21 ** 2 + x * 21 ** 1 + 7
# #     c = 6 * 21 ** 6 + 7 * 21 ** 5 + 5 * 21 ** 4 + 6 * 21 ** 3 + 4 * 21 ** 2 + x * 21 ** 1 + 8
# #     r = a + b + c
# #     if r % 20 == 0:
# #         r = r // 20
# #         s.append(r)
        
# # print(min(s))

# # f = open("C:\\Users\\olesy\\Downloads\\pEdLVpTw_.txt").readlines()
# # for x in range(len(f)):
# #     f[x] = int(f[x])
    
# # s = 0
# # for x in f:
# #     x = abs(x)
# #     if x % 10 == 7:
# #         s += 1
# # k = 0
# # mx = []
# # for x in range(len(f)):
# #     if (f[x] < 0 or f[x + 1]) < 0 and (f[x] > 0 or f[x + 1] > 0) and f[x] + f[x + 1] < s:
# #         k += 1
# #         mx.append(f[x] + f[x + 1])
# # print(k, max(mx))

# #-92
# # n = int(input())
# # zn = 0
# # if n < 0:
# #     zn = 1
# # n = abs(n)
# # n = bin(n)[2:]
# # n = "0" * (8 - len(n)) + str(n)
# # if zn == 0:
# #     print(n)
# # else:
# #     while "0" in n or "1" in n:
# #         if "0" in n:
# #             n = n.replace("0", "1", 1)
# #         if "1" in n:
# #             n = n.replace("1", "=", 1)
# #         if "=" in n:
# #             n = n.replace("=", "0", 1)
# #     print(n)

# №5.2
# s = []
# for n in range(26, 100):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = r + "1"
#         r = "10" + r[2:]
#         s.append(int(r, 2))
#     else:
#         r = r[:-2] + "10"
#         s.append(int(r, 2))
# print(min(s))

# №8.2
# k = 0
# c = 0
# alf = "АБЕКЛ"
# for i1 in alf:
#     for i2 in alf:
#         for i3 in alf:
#             for i4 in alf:
#                 s = i1 + i2 + i3 + i4
#                 k += 1
#                 if s.count("Б") == 1:
#                     c += 1
# print(c)

# №12.2
# for n in range(4, 10000):
#     s = "1" + n * "6"
#     while "111" in s or "66" in s:
#         if "6666" in s:
#             s = s.replace("6666", "1", 1)
#         else:
#             s = s.replace("111", "3", 1)
#         if "66" in s:
#             s = s.replace("66", "6", 1)
#     if s.count("3") >= 5:
#         print(n)
#         break

# №14.1
# n = 7 ** 21 + 49 ** 13 - 7 ** 10
# s = ""
# while n:
#     s = s + str(n % 7)
#     n //= 7
# print(s.count("6"))

# №14.2
# for x in "0123456789ABCDEFG":
#     a = int(f"5432{x}67", 17)
#     b = int(f"302{x}", 17)
#     if (a + b) % 19 == 0:
#         print(int(x, 17))


# №17.2
# f = open("17(4).txt").readlines()

# for x in range(len(f)):
#     f[x] = int(f[x])

# k = 0
# for x in f:
#     if x % 2042 == 0:
#         k += 1
# n = 0
# s = []
# for x in range(len(f) - 1):
#     a = f[x]
#     b = f[x + 1]
#     if a + b > k:
#         n += 1
#         s.append(a + b)
# print(n, max(s))

# f = open("17(2)(1).txt").readlines()
# for x in range(len(f)):
#     f[x] = int(f[x])

# s = -1000000
# for x in f:
#     if x % 36 == 0 and x > s:
#         s = x

    
# for x in range(len(f) - 2):
#     i1 = f[x]
#     i2 = f[x + 1]
#     i3 = f[x + 2]
#     if ((i1 > 0 and int(i1) % 100 == 36) or (i1 > 0 and int(i1) % 100 == 36 and (i1 + i2 + i3) <= s))\
#     :
