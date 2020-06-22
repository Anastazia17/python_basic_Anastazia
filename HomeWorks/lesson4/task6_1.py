# Add task6_1.py

from itertools import count

for el in count(int(input('Введите начальное число: '))):
    if el > 1000:
        break
    else :
        print(el)