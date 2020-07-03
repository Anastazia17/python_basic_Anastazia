# Add task2.py

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def calc_fabric(self):
        pass
    def calc_total(self, other):
        return f'Итого: {float(self.calc_fabric) + float(other.calc_fabric)} м ткани ' \
                f'для пальто {self.name} и костюма {other.name}'

class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
    @property
    def calc_fabric(self):
        result = (float(self.size) / 6.5 + 0.5).__round__(3)
        return result
    def __str__(self):
        return f'1) {self.calc_fabric} м ткани на {self.size} размер для пальто {self.name}'

class Costume(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height
    @property
    def calc_fabric(self):
        result = ((float(self.height) * 2) + 0.3).__round__(3)
        return result
    def __str__(self):
        return f'2) {self.calc_fabric} м ткани на рост {self.height} см для костюма {self.name}'

coat = Coat('Shi-Shi', 42)
print(coat)
costume = Costume('Digel', 187)
print(costume)

print(Clothes.calc_total(coat, costume))