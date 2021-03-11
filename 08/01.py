"""
1. Написать функцию email_parse(<email_address>), 
    которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса 
        и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: 
    подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; 
    имеет ли смысл в данном случае использовать функцию re.compile()?
"""

from re import compile

RFC5322 = r"^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$"
mail_check = compile(RFC5322)

def email_parse(email: str) -> dict:
    """
    Распарсит email адрес.
    Вернет словарь: {
        'username': email,
        'domain': domain,
    }
    """
    matched = mail_check.match(email)
    if matched is None:
        raise ValueError(f'wrong email: {email}')
    return {
        'username': matched[1],
        'domain': matched[2],
    }

if __name__=='__main__':
    print(email_parse('test@test.com'))
    print(email_parse('test test.com'))
