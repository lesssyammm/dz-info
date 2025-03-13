#26

path = "C:\\Users\\olesy\\Desktop\\Файлы\\"
file = "файл к задачам 23 - 27.txt"
f = open(path + file, encoding="utf8")
s = f.readlines()
k = 0
a = []
for i in range(len(s)):
    s[i] = s[i].strip()
    s[i] = s[i].split()
    s[i][-1] = int(s[i][-1])
    if int(s[i][-1]) > 80:
        k += 1
        name = str(s[i][-2][0]) + "."
        a.append((name, s[i][0], s[i][-1]))
a.sort(key=lambda x: x[1])
l = 0
for j in range(k):
    l += 1
    print(str(l) + ")", *a[j])
f.close()

#27

path = "C:\\Users\\olesy\\Desktop\\Файлы\\"
file = "файл к задачам 23 - 27.txt"
f = open(path + file, encoding="utf8")
s = f.readlines()
k = 0
a = []
for i in range(len(s)):
    s[i] = s[i].strip()
    s[i] = s[i].split()
    s[i][-1] = int(s[i][-1])
    if int(s[i][-1]) > 80:
        k += 1
        name = str(s[i][-2][0]) + "."
        a.append((name, s[i][0], s[i][-1]))
a.sort(key=lambda x: x[1])
a.sort(key=lambda y: -y[-1])
l = 0
for j in range(k):
    l += 1
    print(str(l) + ")", *a[j])
f.close()