
"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:

до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.
"""
from time import time
from datetime import datetime


duration = int(input('Enter duration time in seconds: '))

seconds = duration % 60
minutes = duration // 60
print(f'1. {minutes} minutes {seconds} seconds.')

hours = minutes // 60
minutes %= 60
print(f'2. {hours} hours {minutes} minutes {seconds} seconds.')

days = hours // 24
hours %= 24
print(f'3. {days} days {hours} hours {minutes} minutes {seconds} seconds.\n')

utc_time_duration = datetime.utcfromtimestamp(duration)
time_pass = '{years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds'.format(
    years = utc_time_duration.year - 1970,
    months = utc_time_duration.month - 1,
    days = utc_time_duration.day - 1,
    hours=utc_time_duration.hour,
    minutes=utc_time_duration.minute,
    seconds=utc_time_duration.second,
)

utc_time = datetime.utcfromtimestamp(time() + duration)
utc_time.strftime('%Y years, %m months, %d days, %H hours, %M minutes, %S seconds')

print(f'Will pass  {time_pass}')
print(f'Will be {utc_time} UTC')