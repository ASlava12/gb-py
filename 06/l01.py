"""
1. Не используя библиотеки для парсинга, 
    распарсить (получить определённые данные) 
    файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
     — получить список кортежей вида: 
     (<remote_addr>, <request_type>, <requested_resource>). 
    
Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, 
    размер которых превышает объем ОЗУ компьютера.
"""

log_file = '/home/slava/MEGA/projects/geekbrains/gb-py/06/nginx_logs'

def read_line(log_file: str):
    """
    Вернет генератор, который читает переданный ему файл и возвращает кореж: 
        (<remote_addr>, <request_type>, <requested_resource>)
    """
    for line in open(log_file, 'r'):
        temp = line.split(' ')
        # Разбиваем строку лога по пробелам и берем нужные строки: 
        # Пример лога: 91.234.194.89 - - [17/May/2015:08:05:22 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"
        yield temp[0], temp[5][1:], temp[6]

if __name__=='__main__':
    print('[')

    for line in read_line(log_file):
        print(f'{line},')

    print(']')