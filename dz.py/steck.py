def f(s):
    steck = []
    for x in s:
        if x == '(' or x == '{' or x == '[':
            steck.append(x)
        else:
            if len(steck) == 0:
                return False
            else:
                if (steck[-1] == '(' and x == ')') or (steck[-1] == '{' and x == '}') or (steck[-1] == '[' and x == ']'):
                    steck.pop()
    if len(steck) > 0:
        return False
    return True
print(f('{[]}()'))