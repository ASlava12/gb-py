"""
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, 
    если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


>>> a = calc_cube(5)
125
>>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
"""

def val_checker(callback):
    def _wrapper(func):
        def wrapper(*args, **kwargs):
            if not callback(*args, **kwargs):
                if kwargs == {}:
                    raise ValueError(f"wrong args: {', '.join([str(x) for x in args])}")
                else:
                    raise ValueError(f"wrong args: {', '.join([str(x) for x in args])}, {', '.join([str(kwargs[x]) for x in kwargs.keys()])}")
            else:
                return func(*args, **kwargs)
        return wrapper
    return _wrapper

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

print(calc_cube(5))
print(calc_cube(-5))

"""
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py$ python3.8 -i 08/04.py 
125
Traceback (most recent call last):
  File "08/04.py", line 42, in <module>
    print(calc_cube(-5))
  File "08/04.py", line 29, in wrapper
    raise ValueError(f"wrong args: {', '.join([str(x) for x in args])}")
ValueError: wrong args: -5
>>> 
"""