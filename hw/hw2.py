import time

def sm(n):
    k = 0
    d = 1
    step = 1
    if n % 2 == 1:
        step = 2
    while d * d < n:
        if n % d == 0:
            k += d
            k += n // d
        d += step
    if n ** 0.5 == int(n** 0.5):
        k += int(n ** 0.5)
    return k

start = time.time()
k = 0
n = 500_000
while k != 5:
    sm1 = sm(n)
    for i in range(0, 9999):
        for j in range(10):
            dividers_sum = (i * 10 + 7) * 10 + j
            if sm1 == dividers_sum:
                # print(n, sm1)
                k += 1
    n += 1
end = time.time()
print(end - start)