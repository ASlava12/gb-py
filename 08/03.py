"""
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

>>> a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции? 
Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? 
Сможете ли вывести имя функции, например, в виде:
>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""

def type_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        print(f'{func.__name__}(', end='')
        if kwargs != {}:
            print(', '.join(
                [
                    ', '.join([str(type(x)) for x in args]),
                    ', '.join([str(type(kwargs[x])) for x in kwargs.keys()])
                ]
            ), end='')
        else:
            print(', '.join([str(type(x)) for x in args]), end='')
        
        print(f') -> {type(result)}')

        return result

    return wrapper

@type_logger
def calc_cube(x):
   return x ** 3

@type_logger
def test(*args, **kwargs):
    return args, kwargs


print(test(1,2,4, k=1))


"""
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py$ python3.8 -i 08/03.py 
test(<class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>) -> <class 'tuple'>
((1, 2, 4), {'k': 1})
"""