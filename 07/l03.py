"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). 
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html


Примечание: 
    исходные файлы необходимо оставить; 
    обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён); 
    предусмотреть возможные исключительные ситуации; 
    это реальная задача, которая решена, например, во фреймворке django.
"""

from shutil import copytree, rmtree
from os import walk, listdir
from os.path import join as join_path, exists

project_name = 'my_project'

if exists(join_path(project_name, 'templates')):
    rmtree(join_path(project_name, 'templates'))

for root, dirs, files in walk(project_name):
    if 'templates' in dirs and root != project_name:
        for entry in listdir(join_path(root, 'templates')):
            copytree(join_path(root, 'templates', entry), join_path(project_name, 'templates', entry))
"""
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/07$ python3.8 l03.py 
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/07$ tree my_project/templates/
my_project/templates/
├── authapp
│   ├── base.html
│   └── index.html
└── mainapp
    ├── base.html
    └── index.html

2 directories, 4 files
"""