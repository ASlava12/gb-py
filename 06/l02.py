"""
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им 
    запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; 
    код должен работать даже с файлами, размер которых 
    превышает объем ОЗУ компьютера.
"""
from collections import Counter

from l01 import read_line, log_file

remote_addresses = (log_line[0] for log_line in read_line(log_file))
ip_entry_count = Counter(remote_addresses)

def print_top(entry_count_dict: dict, count: int = 10):
    for ip, entry_count in sorted(entry_count_dict.items(), key=lambda item: item[1], reverse=True):
        print(f'IP: {ip}, \tentry count: {entry_count}')
        count -= 1
        if count == 0:
            return

print_top(ip_entry_count)

"""
slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/06$ awk '{print $1}' nginx_logs | sort | uniq -c | sort -nk1 | tail
    532 54.207.57.55
    628 79.136.114.202
   1064 119.252.76.162
   1084 74.125.60.158
   1120 84.208.15.12
   1202 80.91.33.133
   1365 65.39.197.164
   1439 204.77.168.241
   1720 180.179.174.219
   2350 216.46.173.126

slava@slava-Modern-15-A10M:~/MEGA/projects/geekbrains/gb-py/06$ python3.8 l02.py 
IP: 216.46.173.126,     entry count: 2350
IP: 180.179.174.219,    entry count: 1720
IP: 204.77.168.241,     entry count: 1439
IP: 65.39.197.164,      entry count: 1365
IP: 80.91.33.133,       entry count: 1202
IP: 84.208.15.12,       entry count: 1120
IP: 74.125.60.158,      entry count: 1084
IP: 119.252.76.162,     entry count: 1064
IP: 79.136.114.202,     entry count: 628

"""