import itertools
import time


class TrafficLight:
    __color = [['RED', [7, 31]], ['YELLOW', [2, 33]], ['GREEN', [4, 32]], ['YELLOW', [2, 33]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            # print("\ 033 [Режим отображения; цвет переднего плана; цвет фона m ... \ 033 [0m")
            print(f'\r\033[{light[1][1]}m\033{light[0]}\033[0m', end='')
            time.sleep(light[1][0])


traficlight = TrafficLight()
traficlight.running()
