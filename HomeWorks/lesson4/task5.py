# Add task5.py

from functools import reduce

def my_func(el_i, el):
    return el_i * el

print(f'Список всех четных чисел от 100 до 1000: {[el for el in range(100, 1001) if el % 2 == 0]}')
print(f'Результат произведения всех элементов списка: {reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0])}')