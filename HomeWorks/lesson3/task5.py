# Add task5.py

def num_sum ():
    sum_res = 0
    ex_flag = False
    while ex_flag == False:
        numbers = input('Введите числа через пробел или нажмите "q" для выхода из программы: ').split()

        res = 0
        for el in range(len(numbers)):
            if numbers[el] == 'q' or numbers[el] == 'Q':
                ex_flag = True
                break
            else:
                res = res + int(numbers[el])
        sum_res = sum_res + res
        print(f'Текущая сумма: {sum_res}')
    print(f'Финальная сумма: {sum_res}')

num_sum()