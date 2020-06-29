# Add task2.py

class Road:
    _length = None
    _width = None
    weigth = None
    tickness = None

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def intake(self):
        self.weigth = 25
        self.tickness = 0.05
        mass = self._length * self._width * self.weigth * self.tickness / 1000
        print(f'Необходимо {mass} тонн асфальта для строительства дороги.')

road_mass = Road(20, 5000)
road_mass.intake()