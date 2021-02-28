from xml.etree.ElementTree import fromstring
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
    xml_tree = fromstring(get('http://www.cbr.ru/scripts/XML_daily.asp').content)
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