# Add task4.py

def exponentiation_func ():

    while True:
        try:
            x = float(input('Введите любое положительное число: '))
            y = int(input('Введите целое отрицательное число: '))
        except ValueError:
            print('Введены не числа! Попробуйте еще раз.')
            continue

        if x > 0 and y < 0:
            res = x ** y
            return res
            break
        else:
            print ('Введены некорректные числа!')

print (exponentiation_func())