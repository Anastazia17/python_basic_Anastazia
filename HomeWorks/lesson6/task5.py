# Add task5.py

class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'Запуск отрисовки.'

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Выбрана {self.title} - запуск отрисовки.'

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Выбран {self.title} - запуск отрисовки.'

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Выбран {self.title} - запуск отрисовки.'

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())