# Add task3_2.py

while True:
    seasons_dict = {'key_1' : 'зима', 'key_2' : 'весна', 'key_3' : 'лето', 'key_4' : 'осень'}
    month = int(input('Введите порядковый номер месяца: '))

    if month == 1 or month == 12 or month == 2:
        print('Это', seasons_dict.get('key_1'))
    elif month == 3 or month == 4 or month ==5:
        print('Это', seasons_dict.get('key_2'))
    elif month == 6 or month == 7 or month == 8:
        print('Это', seasons_dict.get('key_3'))
    elif month == 9 or month == 10 or month == 11:
        print('Это', seasons_dict.get('key_4'))
    else:
        print('Введен некорректный номер месяца!')
        continue