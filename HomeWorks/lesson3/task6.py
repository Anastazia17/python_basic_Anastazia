# Add task6.py

def int_func():

    word = input('Введите одно слово с маленькой буквы: ')
    print(word.title())
    res_list = []

    while True:
        res_list.append(input('Введите новое слово с маленькой буквы для будущего списка: '))
        res_str = ' '.join(str(e) for e in res_list)
        print (res_str.title())
        continue

int_func()