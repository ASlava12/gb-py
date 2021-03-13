"""
Реализуйте базовый класс Car:
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, ч
    то машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
 
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Вызовите методы и покажите результат.

"""
MAX_TOWNCAR_SPEED = 60
MAX_WORKCAR_SPEED = 40

class Car:
    def __init__(self, speed: float, color: str, name: str, is_police: bool = False):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self, speed = None):
        """
        Изменяет скорость движения автомобиля. 
        Если не передать параметр скорости, то будет использоваться предустановленная при инициализации класса. 
        """
        if speed is not None:
            self._speed = speed
        print(f"Машина {self._name} цвета {self._color} едет со скоростью {self._speed}.")
        return self

    def stop(self):
        """
        Выставляет скорость машины в 0.
        """
        self._speed = 0
        print(f"Машина {self._name} цвета {self._color} остановилась.")
        return self

    def turn(self, direction: str):
        """
        Поворот машины.
        """
        print(f"Машина {self._name} цвета {self._color} повернула на {direction}.")
        return self

    def show_speed(self):
        """
        Выводит текущую скорость автомобиля.
        """
        print(f"Машина {self._name} цвета {self._color} едет со скоростью {self._speed}.")
        return self


class TownCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name)

    def show_speed(self):
        """
        Выводит текущую скорость автомобиля.
        """
        if self._speed <= MAX_TOWNCAR_SPEED:
            print(f"Машина {self._name} цвета {self._color} едет со скоростью {self._speed}.")
        else:
            print(f"Машина {self._name} цвета {self._color} едет со скоростью {self._speed}. Внимание, машина превысила скорость!")
        return self


class WorkCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name)

    def show_speed(self):
        """
        Выводит текущую скорость автомобиля.
        """
        if self._speed <= MAX_WORKCAR_SPEED:
            print(f"Машина {self._name} цвета {self._color} едет со скоростью {self._speed}.")
        else:
            print(f"Машина {self._name} цвета {self._color} едет со скоростью {self._speed}. Внимание, машина превысила скорость!")
        return self


class SportCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name)


class PoliceCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name, is_police=True)


car = Car(70, 'красная', 'test1', is_police=False)
town_car = TownCar(30, 'желтая', 'test2')
work_car = WorkCar(40, 'белая', 'test3')
sport_car = SportCar(30, 'черная', 'test4')
police_car = PoliceCar(30, 'голубая', 'test5')

car.show_speed().turn("лево").stop().go(40).show_speed().turn('право')
town_car.show_speed().turn("лево").stop().go(80).show_speed().turn('право')
work_car.show_speed().turn("лево").stop().go(50).show_speed().turn('право')
sport_car.show_speed().turn("лево").stop().go(120).show_speed().turn('право')
police_car.show_speed().turn("лево").stop().go(90).show_speed().turn('право')

"""
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/09$ python3.8 04.py 
Машина test1 цвета красная едет со скоростью 70.
Машина test1 цвета красная повернула на лево.
Машина test1 цвета красная остановилась.
Машина test1 цвета красная едет со скоростью 40.
Машина test1 цвета красная едет со скоростью 40.
Машина test1 цвета красная повернула на право.
Машина test2 цвета желтая едет со скоростью 30.
Машина test2 цвета желтая повернула на лево.
Машина test2 цвета желтая остановилась.
Машина test2 цвета желтая едет со скоростью 80.
Машина test2 цвета желтая едет со скоростью 80. Внимание, машина превысила скорость!
Машина test2 цвета желтая повернула на право.
Машина test3 цвета белая едет со скоростью 40.
Машина test3 цвета белая повернула на лево.
Машина test3 цвета белая остановилась.
Машина test3 цвета белая едет со скоростью 50.
Машина test3 цвета белая едет со скоростью 50. Внимание, машина превысила скорость!
Машина test3 цвета белая повернула на право.
Машина test4 цвета черная едет со скоростью 30.
Машина test4 цвета черная повернула на лево.
Машина test4 цвета черная остановилась.
Машина test4 цвета черная едет со скоростью 120.
Машина test4 цвета черная едет со скоростью 120.
Машина test4 цвета черная повернула на право.
Машина test5 цвета голубая едет со скоростью 30.
Машина test5 цвета голубая повернула на лево.
Машина test5 цвета голубая остановилась.
Машина test5 цвета голубая едет со скоростью 90.
Машина test5 цвета голубая едет со скоростью 90.
Машина test5 цвета голубая повернула на право.
"""