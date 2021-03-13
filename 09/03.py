"""
Реализовать базовый класс Worker (работник):
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""

class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        if isinstance(income, dict) and 'wage' in income and 'bonus' in income:
            self._income = income
        else:
            raise ValueError(f"Переданы некорректные данные: {income}")

class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, income: dict):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


test_position = Position("Иван", "Иванов", "Инженер", {'bonus': 2000, 'wage': 30000})
print(f"Полное имя позиции: {test_position.get_full_name()}")
print(f"Получит средств: {test_position.get_total_income()}")

"""
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/09$ python3.8 03.py 
Полное имя позиции: Иванов Иван
Получит средств: 32000
"""