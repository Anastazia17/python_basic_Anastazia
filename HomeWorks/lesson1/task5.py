# Add task5.py

profit = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))
if profit > costs:
    print(f'Фирма работает с прибылью. Рентабельность выручки составила: {profit / costs:.2f}')
    employees = int(input('Введите количество сотрудников фирмы: '))
    print(f'Прибыль в расчете на одного сторудника сотавила: {profit / employees:.2f}')
elif profit == costs:
    print('Фирма работает в ноль.')
else:
    print('Фирма работает в убыток.')
