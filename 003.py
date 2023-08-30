#3.Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


import os, math
os.system('cls')

n = float(input('Введите число N = '))
numbers = ''
num = 1
pow = 0
if n >= num:
    while (num <= n):
        numbers += str(f'{num} ')
        pow += 1
        num = int(math.pow(2, pow))
    print(numbers)
else:
    print(f'целые степени двойки не превосходящие {n} отсутствуют')