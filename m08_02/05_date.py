# Написать функцию, которая определяет какой день недели у определенной даты в виде "день-месяц-год".

from datetime import datetime

days_name = {
    0: "понедельник",
    1: "вторник",
    2: "среда",
    3: "четверг",
    4: "пятница",
    5: "суббота",
    6: "воскресенье",
}


def day_of_week(date: str):
    d, m, y = date.split('-')
    date = datetime(day=int(d), month=int(m), year=int(y))
    d_name = days_name.get(date.weekday())
    return d_name


print(day_of_week('31-05-2004'))
print(day_of_week('26-05-1990'))
print(day_of_week('10-12-1980'))
print(day_of_week('11-04-1972'))
