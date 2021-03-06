from sys import argv
from decimal import Decimal, InvalidOperation

from config import db_file, record_size

if __name__=='__main__':
    helps = f"""{argv[0]} PRICE
     - добавляет в файл {db_file} запись о сумме продажи в булочной. Продаж может быть добавлено несколько через пробел. 

    PRICE - сумма продажи. 
    """
    try:
        if len(argv) == 1:
            raise Exception('Нечего добавлять.')
        
        with open(db_file, 'a') as db:
            # Проверяем, возможно ли конвертировать в Decimal
            try:
                for record in [Decimal(x.replace(',', '.')) for x in argv[1:]]:
                    db.write(f'{str(record)[:record_size - 1]:9}\n'.replace('.', ','))
            except InvalidOperation:
                raise Exception('В аргументах нужно передать число!')
        
    except Exception as e:
        print(e, '\n')
        print(helps)