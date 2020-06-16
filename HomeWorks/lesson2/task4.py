# Add task4.py

inquiry = (input('Введите строку для проверки количества элементов и символов: '))
words = []
number = 1
for el in range(inquiry.count(' ') + 1):
    words = inquiry.split()
    if len(str(words)) <= 10:
        print(f' {number} {words [el]}')
        number += 1
    else:
        print(f' {number} {words [el] [0:10]}')
        number += 1