"""
Метод: isdigit
----
1. Найти количество цифр в строке
2. Найти количество чисел в строке
"""

string = "Нильс Бор родился в семье профессора физиологии Копенгагенского университета Христиана Бора (1858—1911), " \
         "дважды становившегося кандидатом на Нобелевскую премию по физиологии и медицине[10], и Эллен Адлер (" \
         "1860—1930), дочери влиятельного и весьма состоятельного еврейского банкира и парламентария-либерала Давида " \
         "Баруха Адлера (дат. David Baruch Adler; 1826—1878) и Дженни Рафаэль (1830—1902) из британской еврейской " \
         "банкирской династии Raphael Raphael & sons[en][11]. Родители Бора поженились в 1881 году. 2"


def count_digits(string):
    count = 0
    for el in string:
        if el.isdigit():
            count += 1
    return count


print(count_digits(string))
print(count_digits(''))


def count_numbers(string):
    count = 0
    pos = 0
    nums = []
    while pos < len(string):
        if string[pos].isdigit():
            num = ''
            while pos < len(string) and string[pos].isdigit():
                num = num + string[pos]
                pos = pos + 1
            nums.append(num)
            count = count + 1
        else:
            pos = pos + 1

    return count, nums


print(count_numbers(string))
print(count_numbers(''))
