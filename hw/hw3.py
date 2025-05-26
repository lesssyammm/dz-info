def count_dividers(n):
    k = 0
    step = 1
    for i in range(999):
        if i == 0:
            d = 4
        else:
            d = int(f"4{i}")
    if n % 2 == 1:
        step = 2
    while d * d < n:
        if n % d == 0:
            k += 2
        d += step
    if n ** 0.5 == int(n ** 0.5):
        k += 1
    if k == 24:
        return 1
    return 0


for n in range(900_000, 10 ** 6):
    if count_dividers(n) == 1:
        print(n)