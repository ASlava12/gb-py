"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. 
К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: 
    для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). П
роверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. 
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
"""

from abc import ABC, abstractmethod, abstractproperty

class Clothes(ABC):
    @abstractmethod
    def __init__(self, param: int):
        pass

    @abstractproperty
    def fabric_amount(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Coat(Clothes):
    def __init__(self, size: int):
        self.__size = size

    @property
    def fabric_amount(self):
        return self.__size / 6.5 + 0.5

    def __str__(self):
        return f"На пальто размера {self.__size} потребуется ткани: {self.fabric_amount:.2f}"


class Suit(Clothes):
    def __init__(self, height: int):
        self.__height = height

    @property
    def fabric_amount(self):
        return self.__height * 2 + 0.3

    def __str__(self):
        return f"На костюм ростом {self.__height} потребуется ткани: {self.fabric_amount:.2f}"

print(
    Coat(24),
    Suit(12),
    sep='\n'
)
