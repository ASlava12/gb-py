"""
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. 
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). 
Убедиться, что ничего лишнего не происходит.
"""

from utils import currency_rates

if __name__=='__main__':
    test = [
        'EUR',
        'USD',
        'INR',
        'UAH',
    ]

    for valute in test:
        rate, date = currency_rates(valute)
        print(f"Текущая стоимость {valute} к рублю: {rate} на дату {date.strftime(r'%d.%m.%Y')}")