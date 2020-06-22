# Add task1.py

from sys import argv
def calc_wage (hours, wage, premium):
    calc_wage = int(hours) * int(wage) + int(premium)
    print(f'Заработная плата сотрудника с учетом премии: {calc_wage} RUB')

try:
    script_name, hours, wage, premium = argv
    calc_wage(hours, wage, premium)

except ValueError:
    print('Введено не три параметра или введены не числа!')