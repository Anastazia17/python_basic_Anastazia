# Add task1.py

def division(*numbers):

    try:
        number1 = float(input('Введите первое число: '))
        number2 = float(input('Введите второе число: '))
        result = number1 / number2
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)

    if number2 != 0:
        return number1 / number2
    else:
        print('На ноль делить нельзя!')

    return result

print(f'result {division()}')