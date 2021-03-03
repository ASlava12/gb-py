"""
1. Написать генератор нечётных чисел от 1 до n (включительно), 
    используя ключевое слово yield, например:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...
"""

def odd_nums(num: int):
    for x in range(1, num + 1, 2):
        yield x

try:
    odd_to_15 = odd_nums(15)
    while True:
        print(next(odd_to_15))
except StopIteration:
    print('done')