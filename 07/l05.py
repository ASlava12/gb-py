"""
*(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, 
в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
    {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }

Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""

from os import scandir
from collections import defaultdict

directory = '.'

stat = defaultdict(lambda : {'count': 0, 'files_extensions': set()})

with scandir(directory) as dir_gen:
    for entry in dir_gen:
        if entry.is_file():
            index = 10 ** len(str(entry.stat().st_size))
            ext = entry.name[entry.name.find('.') + 1:]
            stat[index]['count'] += 1
            stat[index]['files_extensions'].add(ext)


print(dict(stat))

"""
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/07$ python3.8 l05.py 
{10000: {'count': 87, 'files_extensions': {'bin'}}, 100000: {'count': 902, 'files_extensions': {'bin'}}, 1000: {'count': 10, 'files_extensions': {'bin'}}, 10: {'count': 1, 'files_extensions': {'bin'}}}
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/07$ python3.8 l05.py 
{1000: {'count': 1, 'files_extensions': {'yaml'}}, 10000: {'count': 5, 'files_extensions': {'py'}}}
"""