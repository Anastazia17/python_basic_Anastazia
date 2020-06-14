# Add task1.py

el_count = int(input('Укажите количество значений списка для сравнения: '))

result_list = []
i = 0
el = 0

while i < el_count:
    result_list.append(input('Введите следующее значение для сравнения: '))
    i += 1

for value in range(int(len(result_list)/2)):
    result_list[el], result_list[el + 1] = result_list[el + 1], result_list[el]
    el += 2

print(result_list)