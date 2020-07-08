# Add task4-6.py

class Stock:

    def __init__(self, name, cost, quantity, list_number, *args):
        self.name = name
        self.cost = cost
        self.quantity = quantity
        self.list_number = list_number
        self.full_stock = []
        self.list_stock = []
        self.dict_stock = {'Наименование устройства': self.name, 'Стоимость': self.cost, 'Количество на складе': self.quantity}

    def __str__(self):
        return f'{self.name} стоимостью {self.cost} руб. в количестве {self.quantity} шт.'

    def input_stock(self):
        try:
            elem1 = input(f'Введите наименование устройства: ')
            elem2 = int(input('Введите стоимость за штуку: '))
            elem3 = int(input('Введите количество на складе: '))
            device = {'Наименование устройства': elem1, 'Стоимость': elem2, 'Количество на складе': elem3}
            self.dict_stock.update(device)
            self.list_stock.append(self.dict_stock)
            print(f'Текущий список:\n{self.full_stock}')
        except:
            return f'Введены некорректные данные!'
        print('Чтобы продолжить, нажмите Enter\nДля выхода нажмите Q')
        choice = input('')
        if choice == 'Q' or choice == 'q':
            self.full_stock.append(self.list_stock)
            print(f'Товары на складе:\n{self.full_stock}')
            return f'Программа завершена'
        else:
            return Stock.input_stock(self)

class Printers(Stock):
    def print(self):
        return f'Отправить на печать {self.list_number} раз'

class Scanners(Stock):
    def scan(self):
        return f'Отправить на сканирование {self.list_number} раз'

class Copiers(Stock):
    def copier(self):
        return f'Сделать ксерокопию {self.list_number} раз'

elem1 = Printers('Epson', 5600, 5, 10)
elem2 = Scanners('Canon', 3500, 5, 10)
elem3 = Copiers('Xerox', 4000, 1, 15)
print(elem1.input_stock())
print(elem2.input_stock())
print(elem3.input_stock())
print(elem1.print())
print(elem2.scan())
print(elem3.copier())