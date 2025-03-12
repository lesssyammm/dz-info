#11

path = "C:\\Users\\olesy\\Desktop\\Новая папка (2)\\"
with open(path + "11_1.txt", "rt") as f1, open(path + "11_2.txt", "wt") as f2:
    line = f1.readline()
    while line:
        b = bin(int(line))
        o = oct(int(line))
        h = hex(int(line))
        f2.write(b + " " + o + " " + h + "\n")
        line = f1.readline()

# #14

path = "C:\\Users\\olesy\\Desktop\\Новая папка (2)\\"
f1 = open(path + "14.txt", "r")
s = f1.readlines()
s = [int(i) for i in s]
s.sort(key = lambda x: int(str(abs(x))[-1]))
f1.close()
f2 = open(path + "14_2.txt", "w")
f2.write(f'Числа по возрастанию последней цифры: {s}\n')
f2.close()

#16

path = "C:\\Users\\olesy\\Desktop\\Новая папка (2)\\"
with open(path + "16_1.txt", "rt") as f1, open(path + "16_2.txt", "rt") as f2, open(path + "16_3.txt", "wt") as f3:
    line1 = f1.readline()
    line2 = f2.readline()
    while line1 and line2:
        f3.write(line1 + "\n" + line2 + "\n")
        line1 = f1.readline()
        line2 = f2.readline()
        
        