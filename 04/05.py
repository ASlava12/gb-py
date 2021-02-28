"""
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. 
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). Убедиться, что ничего лишнего не происходит.

5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
> python task_4_5.py USD
75.18, 2020-09-05
"""

import sys

from utils import currency_rates

filename, *valutes = sys.argv

for valute in valutes:
    rate, date = currency_rates(valute)
    print(f"{valute}: {rate}, {date.strftime(r'%d.%m.%Y')}")

"""
# Демонстрация: 
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/04$ python3.8 05.py USD EUR 
USD: 74.4373, 27.02.2021
EUR: 90.3743, 27.02.2021
"""