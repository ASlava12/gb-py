"""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (USD, EUR, ...) и возвращающую курс этой валюты по отношению к рублю. 
Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. 

Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа. 
Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать результат числового типа, например float. 

Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? 
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. 
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
"""

import xml.etree.ElementTree as ET

from decimal import Decimal
from requests import get

def get_actual_rates() -> dict:
    """
    Возвращает актуальные значения валюты по отношению к рублю
        в виде словаря "CharCode: Value" 
        
    Информация берется с сайта http://www.cbr.ru/scripts/XML_daily.asp
    """
    result = dict()
    xml_tree = ET.fromstring(get('http://www.cbr.ru/scripts/XML_daily.asp').content)
    for valute in xml_tree:
        valute_rate = 0
        valute_name = ''
        for record in valute:
            if record.tag == 'CharCode':
                valute_name = record.text
            if record.tag == 'Value':
                valute_rate = Decimal(record.text.replace(',', '.'))
        result[valute_name] = valute_rate
    return result

def currency_rates(valute: str, cache: dict = get_actual_rates()) -> Decimal:
    """
    Получить значение валюты
    """
    return cache[valute.upper()]

test = [
    'EUR',
    'USD',
    'INR',
    'UAH',
]

for valute in test:
    print(f'Текущая стоимость {valute} к рублю: {currency_rates(valute)}')