#1

a = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
s = "ЛЮДИ ОХОТНО ВЕРЯТ ТОМУ, ЧЕМУ ЖЕЛАЮТ ВЕРИТЬ"
k = 6
r = ""
for i in s:
    if i not in a:
        r += i
    else:
        r += a[(a.index(i) + k) % 32]
        
print(r)       

#2

a = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
s = input()
k = int(input())
for i in s:
    if i not in a:
        r += i
    else:
        r += a[(a.index(i) + k) % 32]

print(k)

#3

a = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
s = "ХШЖНПУТ ФКХКОЙКТ"

for k in range(1, 32):
    r = ""
    for i in s:
        if i not in a:
            r += i
        else:
            r += a[(a.index(i) - k) % 32]
    print(k, r)
# 5 РУБИКОН ПЕРЕЙДЕН