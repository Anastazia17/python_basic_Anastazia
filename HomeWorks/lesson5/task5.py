# Add task5.py

try:
    with open('test5.txt', 'w+') as my_f:
        line = input('Введите цифры через пробел: \n')
        my_f.writelines(line)
        num_list = line.split()
        print('Сумма введенных чисел:', sum(map(int, num_list)))
except IOError:
    print('Файловая ошибка!')
except ValueError:
    print('Вы ввели не число!')