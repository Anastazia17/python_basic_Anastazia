# Add task4.py

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} поехала'
    def stop(self):
        return f'{self.name} остановилась'
    def turn_right(self):
        return f'{self.name} повернула направо'
    def turn_left(self):
        return f'{self.name} повернула налево'
    def show_speed(self):
        return f'Текущая скорость {self.name} равна {self.speed} км/ч.'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Текущая скорость {self.name} равна {self.speed} км/ч.')
        if self.speed > 40:
            return f'Скорость {self.name} превышена для городского режима.'
        else:
            return f'Скорость {self.name} нормальная для городского режима.'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Текущая скорость {self.name} равна {self.speed} км/ч.')
        if self.speed > 60:
            return f'Скорость {self.name} слишком высока для рабочей машины.'
        else:
            return f'Скорость {self.name} нормальная для рабочей машины.'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def police(self):
        if self.is_police:
            return f'{self.name} - это полицейская машина.'
        else:
            return f'{self.name} - это машина не из полиции.'

lamborghini = SportCar(100, 'Синий', 'Lamborghini', False)
bmv = TownCar(50, 'Черный', 'BMW', False)
niva = WorkCar(70, 'Красный', 'Niva', True)
chance = PoliceCar(110, 'Серебристый',  'Chance', True)
print(f'{niva.turn_right()}.')
print(f'{bmv.turn_left()}, когда {lamborghini.stop()}.')
print(f'{niva.show_speed()}')
print(f'Цвет {niva.name} {niva.color}.')
print(f'{lamborghini.name} - это полицейская машина? {lamborghini.is_police}')
print(f'{niva.name} - это полицейская машина? {niva.is_police}')
print(lamborghini.show_speed())
print(bmv.show_speed())
print(chance.police())
print(chance.show_speed())