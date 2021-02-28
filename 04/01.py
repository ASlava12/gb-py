"""
1. Проверить, установлен ли пакет pillow в глобальном окружении. 
    Если да — зафиксировать версию. Установить самую свежую версию pillow, если ранее она не была установлена. 
    Сделать подтверждающий скриншот. Создать и активировать виртуальное окружение. Убедиться, что в нем нет пакета pillow. 
    Сделать подтверждающий скриншот. Установить в виртуальное окружение pillow версии 6. Сделать подтверждающий скриншот. 
    Деактивировать виртуальное окружение. Сделать подтверждающий скриншот. Скрины нумеровать двухразрядными числами, например: «01.jpg», «02.jpg».
"""
"""
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/04$ pip3.8 freeze | grep -i pillow
Pillow==7.0.0
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/04$ python3.8 -m venv venv
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/04$ source venv/bin/activate
(venv) slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/04$ pip3.8 freeze | grep -i pillow
(venv) slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/04$ pip3.8 install pillow
Collecting pillow
  Downloading Pillow-8.1.0-cp38-cp38-manylinux1_x86_64.whl (2.2 MB)
     |████████████████████████████████| 2.2 MB 2.0 MB/s 
Installing collected packages: pillow
Successfully installed pillow-8.1.0
(venv) slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/04$ pip3.8 freeze | grep -i pillow
Pillow==8.1.0
(venv) slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/04$ deactivate 
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/04$ 
"""

