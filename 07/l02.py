"""
*(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html


Примечание: 
    структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не программно); 
    предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""

from os.path import getsize

from l01 import check_structure, create_project

def get_nested(fstream, result, nested = 0):
    prev = ''
    while fstream.tell() < getsize(fstream.name):
        line = fstream.readline()
        nested_line = line.count(' ')
        if nested_line == nested:
            if line.endswith(':\n'):
                prev = line.strip()[:-1]
                result[prev] = dict()
            else:
                if '__files__' not in result:
                    result['__files__'] = []
                result['__files__'].append(line.strip())
            
        elif nested_line > nested:
            fstream.seek(fstream.tell() - len(line))
            get_nested(fstream, result[prev], nested_line)

        else:
            fstream.seek(fstream.tell() - len(line))
            return


def parse_structure(config: str) -> dict:
    """
    Парсит конфиг и возвращает структуру проекта.
    """
    result = dict()

    with open(config, 'r') as conf:
        get_nested(conf, result)

    return result

if __name__=='__main__':
    dir_structure = parse_structure('config.yaml')
    valid, problems = check_structure(dir_structure)
    if valid:
        create_project(dir_structure)
        print('Структура проекта создана.')
    else:
        print('Обнаружены уже созданные файлы, структура проекта не была создана.\n\tПроблемные файлы:')
        for f in problems:
            print(f'\t\t{f}')

"""
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/07$ python3.8 l02.py 
Структура проекта создана.
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/07$ tree my_project/
my_project/
├── authapp
│   ├── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── authapp
│   │       ├── base.html
│   │       └── index.html
│   └── views.py
├── mainapp
│   ├── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── mainapp
│   │       ├── base.html
│   │       └── index.html
│   └── views.py
└── settings
    ├── dev.py
    ├── __init__.py
    └── prod.py

7 directories, 13 files
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/07$ python3.8 l02.py 
Обнаружены уже созданные файлы, структура проекта не была создана.
        Проблемные файлы:
                my_project
"""