2
def f(n):
    for i in range(1, n):
        h = i
        b = ''
        while h > 0:
            b = str(h % 2) + b
            h //= 2
        if int(b[-1]) == 0:
            s = str(b)
            new = s + '10'
        else:
            s = str(b)
            new = '1' + s + '00'          
        bn = int(new, 2) # перевод из 2 в 10 вид
        if bn > 107:
            return i
        
print(f(100)) #11


5
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((z == w) * (x <= y) or not(w))==0:
                    print(x, y, z, w) #wxzy


6

def f(s, n):
    global k
    if len(s) == n:
        if s.count('Е') == 0 and 'АА' not in s:
            print(k, s)
        k += 1    
    else:
        for c in alf:
            f(s + c, n)

alf = 'АВЕНС'
k = 1
f('', 4) #27

8

def f(n):
    p = 5
    q = 7
    return (p - 1) * (q - 1)

def g(d):
    for d in range(1, 40):
        e = 11
        if (d * e) % f(1) == 1:
            print(d)

print(g(40)) #11 35 берём больший 35


10

s = 6*'3' + 75*'4'
while '35' in s or '355' in s or '3444' in s:
    if '35' in s:
        s.replace('35', '4')
    else:
        if '355' in s:
            s.replace('355', '4')
        else:
            s.replace('3444', '3')
print(s)


11
for x in range(0, 12):
    a = '154' + str(x) + '3'
    b = '1' + str(x) + '365'
    sm = int(a) + int(b)
    if sm % 13 == 0:
        p = sm // 13
        ans = int(str(p), 12)
    
print(ans) #4206

13

a = open('C:\\Users\\olesy\\Downloads\\13.txt').readlines()
d = []
for x in range(len(a)):
    a[x] = int(a[x])
    d.append(a[x])
d.sort(key=lambda x: (x, x % 15 != 0))
n = d[0]
k = 0
mx = 0
e = []
for i in range(len(a)):
    if int(a[i]) % n == 0 and int(a[i + 1]) % n == 0:
        k += 1
        sm = a[i] + a[i + 1]
        if sm > mx:
            mx = sm
print(k) #157

print(mx) #176024