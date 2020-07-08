# Add task7.py

class ComplexNumber:
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        self.z = 'x + y * i'

    def __add__(self, other):
        print(f'Сумма чисел z1 и z2 равна:')
        return f'z = {self.x + other.x} + {self.y + other.y} * i'

    def __mul__(self, other):
        print(f'Произведение чисел z1 и z2 равно:')
        return f'z = {self.x * other.x - self.y * other.y} + {self.y * other.x + self.x * other.y} * i'

    def __str__(self):
        return f'z = {self.x} + {self.y} * i'

z1 = ComplexNumber(5, -7)
z2 = ComplexNumber(2, 4)
print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)