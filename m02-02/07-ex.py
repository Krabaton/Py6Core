line = input('Введите 8 бит: ')

while line != "":
    if line.count('0') + line.count('1') != 8:
        print('Это не 8 бит. Попробуйте ввести еще раз')
    else:
        ones = line.count('1')
        if ones % 2 == 0:
            print('Бит четности равен 0')
        else:
            print('Бит четности равен 1')
    line = input('Введите 8 бит: ')
