"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
    >>> >>> num_translate("one")
    "один"
    >>> num_translate("eight")
    "восемь"

Если перевод сделать невозможно, вернуть None. 
Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
"""

NUMBER_RU = [
    'ноль',
    'один',
    'два',
    'три',
    'четыре',
    'пять',
    'шесть',
    'семь',
    'восемь',
    'девять',
    'десять',
]

NUMBER_EN = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
]

def num_translate(number_str: str) -> str:
    """
    Принимает число от 0 до 10 на английском языке и возвращает перевод на русском.
    """
    if number_str.lower() in NUMBER_EN:
        return NUMBER_RU[NUMBER_EN.index(number_str.lower())]

print(f'num_translate("one"): {num_translate("one")}')
print(f'num_translate("zero"): {num_translate("zero")}')
print(f'num_translate("ten"): {num_translate("ten")}')
print(f'num_translate("abx"): {num_translate("abx")}')
