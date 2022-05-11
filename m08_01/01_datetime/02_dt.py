from datetime import datetime

# Перевод текста в дату и обратно 11.05.2022

td = '11.05.2022'
d = datetime.strptime(td, '%d.%m.%Y')  # %y == 22 %Y == 2022
print(d.date())
print(d.year, d.month, d.day, d.minute)

# Поменять дату
other_d = d.replace(month=4, day=13, hour=14, minute=23, second=12)
print(other_d)
str_d = other_d.strftime('%Y/%d/%m %H:%M:%S')
print(str_d)
