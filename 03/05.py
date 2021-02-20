"""
### Примечание! 

> Написано про два случайных слова, а тут 3! 

5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов, взятых из трёх списков:
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное ДЗ.
"""

from random import randint

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_random_phrase(*args: list) -> list:
    """
    Вернет произвольную фразу, составленную из элементов переданных списков.
    """
    return ' '.join(
        [arg[randint(0, len(arg)-1)] for arg in args]
    )

def make_random_phrase(*args, exclusion=[]) -> str:
    """
    Вернет произвольную фразу, составленную из элементов переданных списков.
    Также, вернет использованные в шутке слова в виде списка. 

    exclusion - список слов, который нужно исключить из шутки. В случае исчерпания слов списке, вернется None.
    """
    result = []
    for arg in args:
        phrase_list = arg.copy()
        for exc in exclusion:
            if exc in phrase_list:
                phrase_list.pop(phrase_list.index(exc))
        
        if phrase_list != []:
            result.append(phrase_list[randint(0,len(phrase_list) - 1)])
        else:
            result.append(str(None))        

    return ' '.join(result), result


def get_jokes(n: int, repeated: bool = True) -> list:
    """
    Вернет список из n шуток, сформированных из случайных слов, взятых из трёх списков:
        nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
        adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
        adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    Флаг repeated - определяет, должно ли слово повторяться.
        False - указывает, что в каждой шутке слова должны быть уникальны. 
    """
    result = []
    exclusion = []
    for _ in range(n):
        if repeated:
            result.append(get_random_phrase(nouns, adverbs, adjectives))
        else:
            phrase, exc = make_random_phrase(nouns, adverbs, adjectives, exclusion=exclusion)
            exclusion.extend(exc)
            result.append(phrase)
    return result



print(f'Тест 10 произвольных шуток (с повторением): {get_jokes(10)}')
print('\n\n')
print(f'Тест 10 произвольных шуток (без повторения): {get_jokes(10, False)}')