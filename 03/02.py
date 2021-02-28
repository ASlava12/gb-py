"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
    >>> >>> num_translate("one")
    "один"
    >>> num_translate("eight")
    "восемь"

Если перевод сделать невозможно, вернуть None. 
Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы. Например:
>>> >>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"
"""

NUMBER_RU = (
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
)

NUMBER_EN = (
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
)

def num_translate_adv(number_str: str) -> str:
    """
    Принимает число от 0 до 10 на английском языке и возвращает перевод на русском.
    """
    if number_str.lower() in NUMBER_EN:
        if ord('A') <= ord(number_str[0]) <= ord('Z'):
            return NUMBER_RU[NUMBER_EN.index(number_str.lower())].capitalize()
        else:
            return NUMBER_RU[NUMBER_EN.index(number_str.lower())]

print(f'num_translate_adv("One"): {num_translate_adv("One")}')
print(f'num_translate_adv("zero"): {num_translate_adv("zero")}')
print(f'num_translate_adv("Ten"): {num_translate_adv("Ten")}')
print(f'num_translate("abx"): {num_translate_adv("abx")}')
