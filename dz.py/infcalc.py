def f(op, l, r):
    if op == '+':
        return l + r
    elif op == '-':
        return l - r
    elif op == '*':
        return l * r
    elif op == '/':
        return l / r


s = input().split() #3 - ( 1 * 1 + 2 ) + 4 * 3 - 3 * ( 1 + 2 * 1 )

stekn = []
stekop = []
i = 0
while i < len(s):
    if s[i].isdigit():
        stekn.append(int(s[i]))
        i += 1
        continue
    if s[i] == '+':
        if len(stekop) == 0 or stekop[-1] == '(':
            stekop.append(s[i])
            i += 1
            continue
        if stekop[-1] in '+-':
            r = stekn.pop()
            l = stekn.pop()
            op = stekop.pop()
            y = f(op, l, r)
            stekn.append(y)
            stekop.append(s[i])
            i += 1
            continue
        if stekop[-1] in '*/':
            r = stekn.pop()
            l = stekn.pop()
            op = stekop.pop()
            y = f(op, l, r)
            stekn.append(y)
    if s[i] == '-':
        if len(stekop) == 0 or stekop[-1] == '(':
            stekop.append(s[i])
            i += 1
            continue
        if stekop[-1] in '+-':
            r = stekn.pop()
            l = stekn.pop()
            op = stekop.pop()
            y = f(op, l, r)
            stekn.append(y)
            stekop.append(s[i])
            i += 1
            continue
        if stekop[-1] in '*/':
            r = stekn.pop()
            l = stekn.pop()
            op = stekop.pop()
            y = f(op, l, r)
            stekn.append(y)