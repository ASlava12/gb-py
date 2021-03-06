#!/usr/bin/env python3
"""
5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, 
    чтобы можно было задать путь к обоим исходным файлам и путь к 
    выходному файлу со словарём. 
Проверить работу скрипта для случая, когда все файлы находятся в 
    разных папках.
"""
import sys
from json import dump

from l03 import to_dict

if __name__=='__main__':
    if len(sys.argv) != 4:
        print(f"Нужно ввести команду в виде: {sys.argv[0]} user_file.csv hobby_file.csv output_file.json")
        
    data = to_dict(sys.argv[1], sys.argv[2])

    with open(sys.argv[3], 'w', encoding='utf-8') as fs:
        dump(
            {','.join(list(k)): ','.join(list(v)) if v is not None else None for k,v in data.items()}, 
            fs, 
            indent=4,
            ensure_ascii=False
        )