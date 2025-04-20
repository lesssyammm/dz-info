    def f(n):
        if n == 1:
            x = int(input())
            return p(x)
        if n == 2:
            dig = float(input())
            c = int(dig)
            b = dig - c
            return b
        if n == 0:
            return