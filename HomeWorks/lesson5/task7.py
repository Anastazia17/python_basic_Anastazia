# Add task7.py

import json

profits = {}
total = {}
prof = 0
average_profit = 0
i = 0

with open('test7.txt', 'r', encoding='UTF-8') as my_f:
    for line in my_f:
        names, firms, income, loss = line.split()
        profits[names] = int(income) - int(loss)
        if profits.setdefault(names) >= 0:
            prof = prof + profits.setdefault(names)
            i += 1
    if i != 0:
        average_profit = prof / i
        print(f'Средняя прибыль всех фирм: {average_profit:.2f}')
    else:
        print(f'Средняя прибыль отсутсвует. Все фирмы в убытке.')
    total = {'Общая средняя прибыль': round(average_profit)}
    profits.update(total)
    print(f'Прибыль каждой компании: {profits}')

with open('test7.json', 'w', encoding='UTF-8') as write_js:
    json.dump(profits, write_js)

    js_str = json.dumps(profits, ensure_ascii=False, separators=(',', ': '), indent=4)
    print(f'Был создан файл json со следующим содержимым:\n'
          f' {js_str}')