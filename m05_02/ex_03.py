'''
Метод: compile

Мы использовали функцию compile чтобы скомпилировать предварительно паттерн. Надо если используем его часто в разных местах программы.
'''

import re

string = "Нильс Бор родился в семье профессора физиологии Копенгагенского университета Христиана Бора (1858—1911), " \
         "дважды становившегося кандидатом на Нобелевскую премию по физиологии и медицине[10], и Эллен Адлер (" \
         "1860—1930), дочери влиятельного и весьма состоятельного еврейского банкира и парламентария-либерала Давида " \
         "Баруха Адлера (дат. David Baruch Adler; 1826—1878) и Дженни Рафаэль (1830—1902) из британской еврейской " \
         "банкирской династии Raphael Raphael & sons[en][11]. Родители Бора поженились в 1881 году..."

# Найти все слова с заглавной буквы
pattern = re.compile(r'[А-ЯA-Z]\w*')
result = pattern.findall(string)
print(result)

# Найти все слова
pattern = re.compile(r'\w+')
result = pattern.findall(string)
print(result)

# Найти слово начала предложения
pattern = re.compile(r'^[А-ЯA-Z]\w*')
result = pattern.findall(string)
print(result)

# Найт слово в конце предложения
result = re.findall(r'\w+.{,3}$', string)
print(result)


# result = re.findall(r'\W+', string)
# print(result)