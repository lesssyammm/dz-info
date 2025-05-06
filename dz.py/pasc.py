# # # from math import factorial


# # # def print_layer(n):
# # #     for k in range(n + 1):
# # #         r = factorial(n) // (factorial(n - k) * factorial(k))
# # #         print(r, end = " ") 


# # # n = int(input("Введите число: "))
# # # if n < 5:
# # #     for i in range(n + 1):
# # #         print(" " * (n - i), end = "")
# # #         print_layer(i)
# # #         print()
# # # else:
# # #     for i in range(n + 1):
# # #         if i != n:
# # #             print(" " * (n + 1 - i), end = "")
# # #             print_layer(i)
# # #             print()
# # #         else:
# # #             print(" " * (0), end = "")
# # #             print_layer(i)
# # #             print()
# # def number_len(n):
# #     k = 1
# #     if n < 0:
# #         k += 1
# #         n = -n
# #     while n // 10 != 0:
# #         k += 1
# #         n = n // 10
    
# #     return k


# # print(number_len(-0))

# def my_factorial(n):
#     if n < 0:
#         return 0
#     k = 1
#     for x in range(2, n+1):
#         k *= x
#     return k


# def my_factorial_recursive(n: int):
#     if n < 0:
#         return -1
#     if n == 0:
#         return 1
#     return n * my_factorial_recursive(n - 1)

# # end = 100
# # for i in range(-1, end):
# #     print(f"{i}! = {my_factorial(i)}")

# # for i in range(-1, end):
# #     print(f"{i}! = {my_factorial(i)}")
# # print(my_factorial(1000))


# print(my_factorial_recursive(1000))
import sys
sys.setrecursionlimit(1000000)


def f(n):
    if n == 41:
        return 41
    if n % 2 == 1:
        return n * f(n - 2)
    if n % 2 == 0:
        return f(n - 1) - n

print(f(9094) // f(9089))