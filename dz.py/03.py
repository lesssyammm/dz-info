#5
from random import randint
    
x = int(randint(1, 100))
guessed = True
while guessed:
    w = int(input("Guess number: "))
    if w < x:
        print('Слишком мало!')
    if w > x:
        print('Слишком много!')
    else:
        guessed = False
        print('Угадал!')


#7

a = [35, 56, 5, 5436, 5, 24, 67, 5, 5, 245] 
n = len(a)
a.sort(key = lambda n: -n)
print(a)
x = int(input())
k = 0
L = 0
R = n
while R - L != 1:
    c = (L + R)//2
    if x < a[c]:
        R = c
    else:
        L = c
        
for i in range(n):
    if a[L - i] == x:
        k += 1
print(k)
