"""
3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера. 
Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
"""


import xml.etree.ElementTree as ET
from dateutil import parser

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
    result['Date'] = parser.parse(xml_tree.attrib['Date'])
    return result

def currency_rates(valute: str, cache: dict = get_actual_rates()) -> Decimal:
    """
    Получить значение валюты и дату последнего обновления 
    """
    return cache[valute.upper()], cache['Date']


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