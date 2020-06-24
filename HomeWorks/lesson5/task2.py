# Add task2.py

with open('test2.txt', encoding='UTF-8') as my_f:
    content = my_f.read()
    print(f'Содержимое файла:\n{content}')

with open('test2.txt', encoding='UTF-8') as my_f:
    content = my_f.readlines()
    print(f'Количество строк в файле: {len(content)}')

with open('test2.txt', encoding='UTF-8') as my_f:
    content = my_f.readlines()
    for i in range(len(content)):
        print(f'Количество символов {i + 1}-ой строки: {len(content[i])}')
# Количество символов в каждой строке, включая переносы строк (они тоже считаются за символы)

with open('test2.txt', encoding='UTF-8') as my_f:
    content = my_f.read()
    content = content.split()
    print(f'Общее количество слов в строках: {len(content)}')