def f(n):
    n = n.replace("3", "4")
    n = n.replace("7", "8")

    k = 1
    for x in n:
        k *= int(x)
    return k


for n in range(1000, 10000):
    if f(str(n)) == 256:
        print(n)
        break