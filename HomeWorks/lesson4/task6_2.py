# Add task6_2.py

from itertools import cycle

i = 0
my_list = ['Анастасия', 777, 'Александр', 'lesson4', 696969]

for el in cycle(my_list):
    if i > 1000:
        break
    else:
        print(el)
        i += 1