"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class ZeroDivision(ZeroDivisionError):
    pass


user_data = 0
while user_data != "":
    user_data = input(">> ")
    try:
        try:
            print(eval(user_data))
        except ZeroDivisionError:
            raise ZeroDivision(f"Была попытка деления на ноль: \"{user_data}\"")
    except ZeroDivision as zd:
        print(zd)


"""
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/11$ python3.8 02.py 
>> 1/2
0.5
>> 2/0
Была попытка деления на ноль: "2/0"
>> 
"""