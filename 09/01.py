"""
Создать класс TrafficLight (светофор):
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
 
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep

class TrafficLight:
    colors = ('red', 'yellow', 'green')
    waits = {
        'red': 7, # Переключение с красного на желтый
        'yellow': 2, # Переключение с желтого
        'green': 5 # Переключение с зеленого на желтый
    }
    def __init__(self):
        self.__color = 'red'
        self.__previous = 'yellow'

    def _new_color(self, color):
        sleep(self.waits[self.__color])
        self.__previous = self.__color
        self.__color = color
        print(f'Цвет световора изменился с {self.__previous} на {self.__color}.')

    def running(self, color: str):
        if  (self.__color == 'red' or self.__color == 'green') and color == 'yellow':
            self._new_color(color)
            return self
        elif (color == 'red' or color == 'green') and self.__color == 'yellow':
            self._new_color(color)
            return self
        raise ValueError(f'Был передан некорректный цвет: {color}, в данный момент установлен {self.__color}')

traffic_light = TrafficLight()

traffic_light.running('yellow').running('green').running('yellow').running('red')

traffic_light.running('green')
"""
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/09$ python3.8 -i 01.py 
Цвет световора изменился с red на yellow.
Цвет световора изменился с yellow на green.
Цвет световора изменился с green на yellow.
Цвет световора изменился с yellow на red.
Traceback (most recent call last):
  File "01.py", line 44, in <module>
    traffic_light.running('green')
  File "01.py", line 38, in running
    raise ValueError(f'Был передан некорректный цвет: {color}, в данный момент установлен {self.__color}')
ValueError: Был передан некорректный цвет: green, в данный момент установлен red
>>> 
"""
