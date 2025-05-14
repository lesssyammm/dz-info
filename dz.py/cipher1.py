# a = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
# s = "ПРИШЕЛ УВИДЕЛ ПОБЕДИЛ"
# k = "ЗАБЕГ"
# r = ""
# h = 0

# for i in s:
#     if i not in a:
#         r += i
#     else:
#         i = a[(a.index(i) + a.index(k[h % len(k)])) % len(a)]
#         r += i
#         h += 1

# print(r)


#1

a = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
s = "ПРИШЕЛ УВИДЕЛ ПОБЕДИЛ"
k = ""
r = "ЩЫЖППЦ СЩТПГВ ЩЩЯЬОУЙ"
h = 0

for i in s:
    if i not in a:
        k += i
    else:
        i = a[(len(a) - a.index(i) + a.index(r[h])) % len(a)]
        k += i
    h += 1

print(k) #ключ


#2

a = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
s = "ПРИШЕЛ УВИДЕЛ ПОБЕДИЛ"
k = ""
r = "ЗШЬИУН УПРЙЭУ ГЮПЗДХУ"
h = 0

for i in s:
    if i not in a:
        k += i
    else:
        i = a[(len(a) - a.index(i) + a.index(r[h])) % len(a)]
        k += i
    h += 1

print(k) #шифрование


#3

a = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
s = "ПРИШЕЛ УВИДЕЛ ПОБЕДИЛ"
k = ""
r = "ЧЭЬЖХЧ УФРОЕУ ЬВПХРИЭ"
h = 0

for i in s:
    if i not in a:
        k += i
    else:
        i1 = a[(len(a) - a.index(i) + a.index(r[h])) % len(a)]
        k += i1
    h += 1

print(k) #информатика

#4

a = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
s = ""
k = "КРИПТОСТОЙКОСТЬ"
r = "ЭБЪЭЫЕЩФЬЪЬК ЙЪРЪР Т ЯТЯЙЪВЩШРЫЧ ЭПЧ ПЬТЫЩС ШФИЕС"
h = 0

for i in r:
    if i not in a:
        s += i
    else:
        i1 = a[(len(a) - a.index(k[h % len(k)]) + a.index(i)) % len(a)]
        s += i1
        h += 1

print(s) #УСТОЙЧИВОСТЬ ШИФРА К РАСШИФРОВКЕ БЕЗ ЗНАНИЯ КЛЮЧА
