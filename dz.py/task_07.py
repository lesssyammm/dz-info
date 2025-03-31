x = '- 5 + 6 - 7 + 8 9'
x = x[::-1]
x = x.split()
print(x)
steck = []
for i in x:
    if i.isdigit():
        steck.append(int(i))
    else:
        r = steck.pop()
        l = steck.pop()
        if i == '+':
            a = r + l
        elif i == '-':
            a = r - l  
        elif i == '*':
            a = r * l
        elif i == '/':
            a = r // l
        steck.append(a)
print(steck.pop())