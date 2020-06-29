# Add task1.py

from time import sleep

class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный']

    def running(self):
        i = 0
        while i < 3:
            print(f'Режим светофора изменен на '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()