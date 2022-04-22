'''
Задача: Поиск phone
Метод: match - ищет только вначале строки!!! аналог search

шаблон следующий: +380(67)777-7-777 или +380(67)777-77-77
'''

import re

phones = ['+380(66)964-0-547', '+06(37)306465', '+380(96)193-51-71', '+63264-3-973',
          '+50832-52-00', '+000000000', '+487(30)283-9-18', '(98)622-35-75', '+380(29)794-7963']

pattern = r'\+380\(\d{2}\)\d{3}-\d-\d{3}|\+380\(\d{2}\)\d{3}-\d{2}-\d{2}|\+380\(\d{2}\)\d{3}-\d{4}'

for phone in phones:
    print(f'{phone} is valid: {bool(re.match(pattern, phone))}')
