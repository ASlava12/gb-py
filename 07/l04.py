"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, 
    в котором ключи — верхняя граница размера файла (пусть будет кратна 10), 
    а значения — общее количество файлов (в том числе и в подпапках), 
    размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), 

    например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }

Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

from os import scandir
from collections import defaultdict

directory = 'some_data'

stat = defaultdict(lambda : 0)

for entry in scandir(directory):
    if entry.is_file():
        stat[10 ** len(str(entry.stat().st_size))] += 1

print(dict(stat))

"""
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/07$ python3.8 l04.py 
{10000: 87, 100000: 902, 1000: 10, 10: 1}
"""