"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp


Примечание: 
    подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
    как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; 
    можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""

"""
подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);

 Ответ: вызвать исключение и сообщить, какие файлы / папки уже есть
"""

from os import mkdir
import os.path as path

from collections import defaultdict

dir_structure = {
    'my_prject': {
        'settings': {},
        'mainapp': {},
        'adminapp': {},
        'authapp': {},
    }
}

def check_structure(dir_structure: dict) -> (bool, dict):
    """
    Проверяет переданную структуру директории проекта и проверяет наличие файлов / директорий, которые пересекаются со структурой.

    Возвращает True, [] если файлов нет и False, [список существующих директорий / файлов], если найдено совпадение.
    """
    
    result = True
    crossed = []

    for directory in dir_structure.keys():
        if path.exists(directory):
            if result:
                result = False
            crossed.append(directory)
    
    return result, crossed

def create_project(dir_structure: dict, joined = ''):
    """
    Создает проект на основе вложенности словаря dir_structure. 
    
    joined - префикс к директории. 
    """
    for directory in dir_structure.keys():
        if directory != '__files__':
            mkdir(path.join(joined, directory))
            create_project(dir_structure[directory], path.join(joined, directory))
        else:
            for name in dir_structure['__files__']:
                open(path.join(joined, name), 'w').close()

if __name__=='__main__':
    valid, problems = check_structure(dir_structure)
    if valid:
        create_project(dir_structure)
        print('Структура проекта создана.')
    else:
        print('Обнаружены уже созданные файлы, структура проекта не была создана.\n\tПроблемные файлы:')
        for f in problems:
            print(f'\t\t{f}')

"""
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/07$ python3.8 l01.py 
Структура проекта создана.
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/07$ ll my_prject/
итого 24
drwxrwxr-x 6 slava slava 4096 мар  7 10:55 ./
drwxrwxr-x 3 slava slava 4096 мар  7 10:55 ../
drwxrwxr-x 2 slava slava 4096 мар  7 10:55 adminapp/
drwxrwxr-x 2 slava slava 4096 мар  7 10:55 authapp/
drwxrwxr-x 2 slava slava 4096 мар  7 10:55 mainapp/
drwxrwxr-x 2 slava slava 4096 мар  7 10:55 settings/
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/07$ python3.8 l01.py 
Обнаружены уже созданные файлы, структура проекта не была создана.
        Проблемные файлы:
                my_prject
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/07$ 
"""