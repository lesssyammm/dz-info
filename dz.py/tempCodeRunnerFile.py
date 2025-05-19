import random


# def printMatrix01(A):
#     for row in A:
#         for x in row:
#             print("{:4}".format(x), end="")
#         print()

        
# def printMatrix02(A):
#     for i in range(len(A)):
#         for j in range(len(A[i])):#A[i] = номер столбца, число элементов в строке i
#             print("{:4}".format(A[i][j]), end="")
#         print()


# N = 3
# M = 2
# A = [[0] * M for i in range(N)]
# for i in range(N):
#     for j in range(M):
#         A[i][j] = random.randint(20, 80)

# printMatrix01(A)
# print()
# printMatrix02(A)

# sm = 0
# for i in range(N):
#     for j in range(M):
#         sm += A[i][j]
# print(sm)

# for row in A:
#     sm += sum(row)
# print(sm) #сумма всей матрицы

#1

def printMatrix(a):
    for row in a:
        for x in row:
            print("{:4}".format(x), end="")
        print()


n = int(input())
m = int(input())
a = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = random.randint(10, 99)

printMatrix(a)

total = 0
for row in a:
    for x in row:
        if x % 2 == 0:
            total += 1
print(total)