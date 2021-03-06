from sys import argv
from decimal import Decimal, InvalidOperation
from os.path import getsize

from config import db_file, record_size

def read_records(file, start: int, end: int):
    with open(file, 'r') as db:
        # Первый элемент для вывода
        FIRST = start if start != -1 else 1

        all_elements = getsize(file) // record_size
        # Последний элемент
        EOF = end + 1 if end != -1 else all_elements + 1

        if all_elements < end or all_elements < start:
            raise Exception(f'Передан слишком большой идентификатор записи. Всего записей: {all_elements}')

        if start > end and start != -1 and end != -1:
            raise Exception(f'Параметр FROM ({start}) должен быть меньше параметра TO ({end})!')

        if start != -1:
            db.seek((start - 1) * record_size)

        for num, record in ((x, db.read(record_size)) for x in range(FIRST, EOF)):
            yield num, record.rstrip()

if __name__=='__main__':
    helps = f"""{argv[0]} [FROM [TO]]
     - читает из файла {db_file} записи о сумме продажи в булочной. 

    FROM - с какого номера выводить записи.
        Все записи начинаются с 1.
    TO - по какой номер выводить записи.

    Чтобы прочитать все записи - нужно запустить скрипт без аргументов.
    """
    try:
        # Проверяем, возможно ли конвертировать аргументы в int
        id_from = -1
        id_to = -1
        try:
            if len(argv) > 1:
                id_from = int(argv[1])
                if 0 > id_from:
                    raise Exception('Параметр FROM должен быть больше 0!')
            if len(argv) > 2:
                id_to = int(argv[2])
                if 0 > id_to:
                    raise Exception('Параметр TO должен быть больше 0!')
        except ValueError:
            raise Exception('В аргументах нужно передать целое число!')

                 
        for record in read_records(db_file, id_from, id_to):
            print(record)
                
        
    except Exception as e:
        print(e, '\n')
        print(helps)