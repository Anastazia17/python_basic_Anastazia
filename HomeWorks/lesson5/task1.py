# Add task1.py

with open('test1.txt', 'w') as my_f:
    data = input('Введите текст: ')
    while data:
        my_f.writelines(data + '\n')
        data = input('Введите текст: ')
        if data == None:
            break

with open('test1.txt') as my_f:
    for line in my_f:
        print(line)