# Add task2.py

class DivisionByZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return f'Делить на ноль нельзя!'

a = DivisionByZero(1, 2)
print(DivisionByZero.divide_by_zero(100, 0))
print(DivisionByZero.divide_by_zero(56.98, 0.25))
print(a.divide_by_zero(77, 0))