with open("C:\\Users\\olesy\\Desktop\\Новая папка\\4.txt") as a:
    s = a.readlines()
    for i in range(len(s)):
        s[i] = s[i].strip()
    ln = max(s, key=lambda x: x.count('Q'))
    
    d = {}
    for x in ln:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    
    a1 = list(d.items())
    a1.sort(key=lambda x: x[1])
    #print(a1[0][0])
    ln2 = max(s, key=lambda x: x.count('Q'))
    p = 0
    for j in ln2:
        j = int(j)
        p += j
    print((a1[0][0]), p)