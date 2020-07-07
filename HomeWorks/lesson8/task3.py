# Add task3.py

class ErrNotNumber:
    def __init__(self, *args):
        self.new_list = []
    def new_input(self):
        while True:
            try:
                list_item = int(input('Введите любое число и нажмите Enter: '))
                self.new_list.append(list_item)
                print(f'Текущий список: {self.new_list} \n')
            except:
                print(f'Введено не число!')
                y_n = input(f'Попробуете еще раз? Нажмите Y/N: ')
                if y_n == 'Y' or y_n == 'y':
                    print(try_except.new_input())
                elif y_n == 'N' or y_n == 'n':
                    print(f'Текущий список: {self.new_list}')
                    return f'Вы вышли из программы.'
                else:
                    return f'Введено некорректное значение!\nПрограмма продолжает работу.'
                    print(try_except.new_input())

try_except = ErrNotNumber(1)
print(try_except.new_input())