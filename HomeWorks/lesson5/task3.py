# Add task3.py

with open('test3.txt', encoding='UTF-8') as my_f:

    workers = []
    lines = my_f.readlines()

    for i in range(len(lines)):
        employee = lines[i].split()[0]
        wage = float(lines[i].split()[1])
        workers.append(wage)
        if wage < 20000.00:
            print(f'Оклад менее 20000 руб., а именно {wage} руб. у сотрудника: {employee}.')
    print('Средний оклад сотрудников:', sum(workers) // len(workers), 'руб.')