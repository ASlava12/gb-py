"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, 
    а в другом — данные об их хобби. Известно, что при хранении 
    данных используется принцип: одна строка — один пользователь, 
    разделитель между значениями — запятая. Написать код, 
    загружающий данные из обоих файлов и формирующий из них словарь: 
    ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. 
    Проверить сохранённые данные. 

    Если в файле, хранящем данные о хобби, меньше записей, 
        чем в файле с ФИО, задаём в словаре значение None. 
        Если наоборот — выходим из скрипта с кодом «1». 
    При решении задачи считать, что объём данных в файлах во много 
        раз меньше объема ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""

users_file = 'users.csv'
hobby_file = 'hobby.csv'

def get_data(data_file):
    """
    Возвращает кортеж элементы которого формируются по разделителю - ','
    """
    for data_line in open(data_file, 'r'):
        yield tuple(data_line.replace('\n', '').split(','))

def to_dict(users_file: str, hobby_file: str) -> dict:
    """
    Формирование словаря из переданных файлов
    """
    result = dict()

    users_g = get_data(users_file)
    hobby_g = get_data(hobby_file)

    for hobby in hobby_g:
        try:
            result[next(users_g)] = hobby
        except StopIteration:
            exit(1)
    
    for users in users_g:
        result[users] = None

    return result

if __name__=='__main__':
    print(to_dict(users_file, hobby_file))