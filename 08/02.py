"""
2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения информации вида: 
    (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>), например:

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
Примечание: 
    вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки? 
    Можно ли для них уточнить регулярное выражение?
"""
import os.path as path
from sys import argv
from re import compile

log_file = path.join(path.dirname(path.dirname(path.realpath(argv[0]))), '06/nginx_logs')

NGINX_LOG = r"^(.*) .* .* \[(.*)\] \"(.*) (.*) (.*)\" (.*) (.*) \"(.*)\" \"(.*)\"$"
log_row = compile(NGINX_LOG)

def get_log_record(log_file: str):
    with open(log_file, 'r') as f:
        for line in f:
            res = log_row.match(line)
            yield (
                res[1],
                res[2],
                res[3],
                res[4],
                res[6],
                res[7]
            )

test = get_log_record(log_file)

for x in range(10):
    print(next(test))