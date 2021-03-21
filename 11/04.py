"""
4. Начните работу над проектом «Склад оргтехники». 
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. 

Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 

В базовом классе определите параметры, общие для приведённых типов. 

В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
"""
from enum import Enum

class InventoryCollision(Exception):
    def __init__(self, storage_model, inventory_number):
        super().__init__(f"В складе {storage_model} уже присутствует техника с инвентаризационным номером: {inventory_number}.")


class Equipment:
    def __init__(self, inventory_number: str, model: str, description: str, equipment_type: str):
        self.__inventory_number = inventory_number
        self.__model = model
        self.__description = description
        self.__type = equipment_type

    @property
    def inventory_number(self):
        return self.__inventory_number
    
    @property
    def model(self):
        return self.__model

    @property
    def description(self):
        return self.__description

    @property
    def type(self):
        return self.__type


class Storage:
    def __init__(self, model, location):
        """
        Создает склад с местоположением {location}.
        """
        self.__location = location
        self.__storage = {}

    def getLocation(self):
        return self.__location

    def place(self, equipment: Equipment):
        self.__storage[equipment.get_inventory_number()] = equipment
        return self

    def take(self, inventory_number: str):
        equipment = self.__storage[inventory_number]
        del(self.__storage[inventory_number])
        return equipment

    def get_storage_list(self, equipment_type: str = None):
        return {
            inventory_number: equipment 
            for inventory_number, equipment in self.__storage.items() 
                if equipment.type == equipment_type or equipment_type is None
        }

    def get_equipments_types(self):
        equipments_types = set()
        for equipment in self.__storage.values():
            equipments_types.add(equipment.type)
        return equipments_types

class PrinterTypes(Enum):
    laser = 1
    led = 2
    jet = 3


class Printer(Equipment):
    def __init__(self, inventory_number: str, model: str, description: str, printer_type: PrinterTypes):
        super().__init__(inventory_number, model, description, "printer")
        self.__species = printer_type

    @property
    def species(self):
        return self.__species


class Scaner(Equipment):
    def __init__(self, inventory_number: str, model: str, description: str):
        super().__init__(inventory_number, model, description, "scaner")


class Xerox(Equipment):
    def __init__(self, inventory_number: str, model: str, description: str):
        super().__init__(inventory_number, model, description, "xerox")


class Computer(Equipment):
    def __init__(self, inventory_number: str, model: str, description: str, internal_components: list):
        super().__init__(inventory_number, model, description, "computer")
        # Внутренние компоненты можно заменять
        self.internal_components = internal_components


class MonitorTypes(Enum):
    crt = 1
    lcd = 2
    les = 3
    plasma = 4


class Monitor(Equipment):
    def __init__(self, inventory_number: str, model: str, description: str, monitor_type: MonitorTypes, frame_rate: int = 60):
        super().__init__(inventory_number, model, description, "monitor")
        self.__species = monitor_type
        self.__frame_rate = frame_rate

    @property
    def species(self):
        return self.__species

    @property
    def frame_rate(self):
        return self.__frame_rate

