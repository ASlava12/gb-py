"""
Осуществить программу работы с органическими клетками, состоящими из ячеек. 
Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр, 
    соответствующий количеству ячеек клетки (целое число). В классе должны быть 
    реализованы методы перегрузки арифметических операторов: 
        сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), 
        деление (__floordiv____truediv__()). 
    
    Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, 
        умножение и округление до целого числа деления клеток соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться 
    сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность 
    количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение 
    количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как 
    целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. 
В этом случае метод make_order() вернёт строку: *****\n*****\n**.
Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. 
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке: https://pythonworld.ru/osnovy/peregruzka-operatorov.html

"""
from math import ceil

class Cell:
    cells_total = 0

    def __init__(self, count: int = 1):
        if count < 1:
            raise ValueError(f"Нужно указать количество клеток больше 0. Указано: {count}")
        if type(count) != int:
            raise TypeError(f"Нужно указать целое количество клеток. Указано: {count}")
        self._count = count
        Cell.cells_total += 1
        self._name = f"№{Cell.cells_total}"

    def __add__(self, cell):
        return Cell(self._count + cell._count)
    
    def __sub__(self, cell):
        if self._count <= cell._count:
            raise ValueError(f"У вычитаемой клетки меньше ячеек: {self._count} <= {cell._count}")
        return Cell(self._count - cell._count)
    
    def __mul__(self, cell):
        return Cell(self._count * cell._count)

    def __floordiv__(self, cell):
        return Cell(self._count // cell._count)

    def __truediv__(self, cell):
        return Cell(self._count // cell._count)

    def make_order(self, row_length):
        max_row_length = "*" * row_length
        remain = self._count % row_length
        total_rows = ceil(self._count / row_length)
        return "\n".join([
            max_row_length if (remain != 0) and (i < total_rows) else "*" * (remain)
                for i in range(1,total_rows + 1)
        ])

    def __str__(self):
        return f"Клетка {self._name} имеет ячеек: {self._count}"


cell_list = [
    Cell(59), 
    Cell(14),
]

cell_list.append(cell_list[0] + cell_list[1])
cell_list.append(cell_list[0] - cell_list[1])
cell_list.append(cell_list[0] / cell_list[1])
cell_list.append(cell_list[0] // cell_list[1])
cell_list.append(cell_list[0] * cell_list[1])

for cell in cell_list:
    print(cell, "Вывод ячеек по рядам:", cell.make_order(10), "\n", sep='\n')
