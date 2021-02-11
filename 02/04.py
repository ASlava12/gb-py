"""
4. Создать список, содержащий цены на товары (10–20 товаров), например:

[57.8, 46.51, 97, ...]
* Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

* Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
* Создать новый список, содержащий те же цены, но отсортированные по убыванию.
* Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""

from random import random


count = 20
max_price = 1000
# создаем список со случайными ценами на товар в пределах от 0 до 1000 рублей
prices = [f'{random() * max_price:.2f}' for x in range(count)]

def print_price(prices):
    count = len(prices)
    for index in range(count):
        dot = prices[index].find('.')
        rubles = prices[index][:dot]
        penny = prices[index][dot + 1:]

        price = f'{rubles} руб {penny} коп'

        if index + 1 < count:
            print(price, end=', ')
        else:
            print(price, end='\n\n')

print_price(prices)

prices.sort(key=lambda x: float(x))

print_price(prices)

prices_new = prices.copy()
prices_new.sort(key=lambda x: float(x), reverse=True)

print('Первый список: ', end='')
print_price(prices)
print('Второй список: ', end='')
print_price(prices_new)

print('5 самых дорогих товаров: ', end='')
print_price(prices[-5:])