'''Проверка, простое ли число'''
from math import *   # лучше использовать import math  чтобы не было конфликтов в названии переменных

n = input('Введите диапозон:- ')
p = [2, 3]
count = 2
a = 5

while (count<int(n)):
    b = 0
    for i in range(2,a):
        if i <= sqrt(a):
            if (a%i == 0):
                print('a, непростое',a)
                b = 1
            else:
                pass
    if (b != 1):
        print('a, простое',a)
        p = p + [a]
    count = count + 1
    a = a + 2
print (p)
