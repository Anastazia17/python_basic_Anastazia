# Add task3_1.py

while True:
    seasons_list = ['зима', 'весна', 'лето', 'осень']
    month = int(input('Введите порядковый номер месяца: '))

    if month == 1 or month == 12 or month == 2:
        print('Это', seasons_list[0])
    elif month == 3 or month == 4 or month ==5:
        print('Это', seasons_list[1])
    elif month == 6 or month == 7 or month == 8:
        print('Это', seasons_list[2])
    elif month == 9 or month == 10 or month == 11:
        print('Это', seasons_list[3])
     else:
        print('Введен некорректный номер месяца!')
        continue