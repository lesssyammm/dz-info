#1

path = "C:\\Users\\olesy\\Desktop\\Файлы\\"
f = open(path + "файл к задачам 19 и 21(1).txt", encoding="utf8")
s = f.readlines()
f.close()
for i in range(len(s)):
    s[i] = s[i].strip()
s = " ".join(s)
s = s.split()
n = 0
for j in s:
    if len(j) > n:
        n = len(j)
        st = j
print(st)
f.close()

#2

path = "C:\\Users\\olesy\\Desktop\\Файлы\\"
file = "файл к задачам 19 и 21(1).txt"
f1 = open(path + file, encoding="utf8")
s = f1.readlines()
for i in range(len(s)):
    s[i] = s[i].strip()
    
s = " ".join(s).lower()
s = s.split()
f1.close()
f2 = open(path + "new.txt", "w")
a = []
for j in s:
    if j[0] == "И" or j[0] == "и":
        f2.write(j + "\n")
        a.append(j)

print(len(a)) #4195
f2.close()

#3

path = "C:\\Users\\olesy\\Desktop\\Файлы\\"
file = "файл к задачам 19 и 21(1).txt"
f1 = open(path + file, encoding="utf8")
s = f1.readlines()
for i in range(len(s)):
    s[i] = s[i].strip()
    
s = " ".join(s).lower()
s = s.split()
f1.close()

f2 = open(path + "new2.txt", "w")
a = []
for x in s:
    for j in range(len(x)):
        if len(x) % 2 == 0:
            if x[0:j//2] == x[len(x):j//2:-1]:
                f2.write(x + "\n")
                if x not in a:
                    a.append(x)
        else:
            if x[0:j//2 + 1] == x[len(x):j//2 + 1:-1]:
                f2.write(x + "\n")
                if x not in a:
                    a.append(x)
print(*a)
print(len(a)) #как еще или тут тот iii летел еле оно ими обо иди и-и мадам ото уху xix комок
#18
f2.close()
