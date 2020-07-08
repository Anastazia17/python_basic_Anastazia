# Add task4-6.py

from random import choice

class Storage:
    types = ['Printers', 'Scanners', 'Xeroxes']
    stock = {}
    departmens = ['Отдел продаж', 'Отдел развития', 'Отдел разработки',
                  'Отдел качества', 'Отдел маркетинга', 'Отдел кадров', 'Отдел бухгалтерии']

    @classmethod
    def tech_entry(cls, other):
        try:
            if other.type not in cls.types:
                raise UserWarning('Технику такого типа нельзя принять на склад!')
            else:
                if other.model in cls.stock:
                    cls.stock[other.model][1]+=other.amount
                else:
                    cls.stock[other.model] = [other.type, other.amount]
                print(f'Техника {other.model} принята на склад в количестве {cls.stock[other.model][1]} штук.')
        except UserWarning as e:
            print(e)

    @classmethod
    def tech_transfer(cls):
        for model, item in cls.stock.items():
            the_type = item[0]
            if the_type == 'Printers':
                if cls.stock[model][1] == 0:
                    print(f'На складе нет техники {model} для передачи!')
                else:
                    cls.stock[model][1]-=1
                    print(f'Техника {model} передана в {choice(cls.departmens)}.')
            if the_type == 'Scanners':
                if cls.stock[model][1] == 0:
                    print(f'На складе нет техники {model} для передачи!')
                else:
                    cls.stock[model][1]-=1
                    print(f'Техника {model} передана в {choice(cls.departmens)}.')
            if the_type == 'Xeroxes':
                if cls.stock[model][1] == 0:
                    print(f'На складе нет техники {model} для передачи!')
                else:
                    cls.stock[model][1] -= 1
                    print(f'Техника {model} передана в {choice(cls.departmens)}.')
        print()

class OfficeTech():
    def __init__(self, model, amount, type):
        self.model = model
        self.amount = int(amount)
        self.type = type

class Printers(OfficeTech):
    def __init__(self, model, amount, type='Printers'):
        super().__init__(model, amount, type=type)

class Scanners(OfficeTech):
    def __init__(self, model, amount, type='Scanners'):
        super().__init__(model, amount, type=type)
        self.amount = amount

class Xeroxes(OfficeTech):
    def __init__(self, model, amount, type='Xeroxes'):
        super().__init__(model, amount, type=type)
        self.amount = amount

pri1 = Printers('HP LaserJet Pro M304a', 7)
pri2 = Printers('Epson L132', 3)
sca1 = Scanners('CanoScan LiDE 300', 9)
sca2 = Scanners('HP ScanJet Pro 2500 f1', 4)
xer1 = Xeroxes('Xerox WorkCentre 3025BI', 6)
xer2 = Xeroxes('PANTUM P2200', 5)

# Вносим товары в список для отправки на склад.
stock_list = [pri1, pri2, sca1, sca2, xer1, xer2]
for el in stock_list:
    Storage.tech_entry(el)
print()

# Находим максимальное количество определенной модели техники, чтобы отправить всё со склада.
checker = []
for value in Storage.stock.values():
    checker.append(value[1])
iterations = max(checker)

# Распределяем технику по отделам пока не опустошим склад полностью.
for i in range(iterations):
    Storage.tech_transfer()

print('Вся техника отправлена. Склад пуст.')
for el, vel in Storage.stock.items():
    print(el, vel)