# Add task7.py

from math import factorial
from itertools import count

def my_gen():
    for el in count(1):
        yield factorial(el)

new_gen = my_gen()
c = 0
for i in new_gen:
    if c > 100:
        break
    else:
        print(i)
        c += 1