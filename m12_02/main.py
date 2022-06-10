import shelve


class AwesomeClass:
    awesome = True


class Dummy:
    default = 0

    def __init__(self, value):
        self.default = value


aw = AwesomeClass()
dum = Dummy(42)

filename = 'database/some_db'

with shelve.open(filename) as db:
    db['awesome'] = aw
    db['dummy'] = dum
    db['my_list'] = [1, 2, 3, 4]
    # db['my_list'].append(5)
    # Способ обновить значение
    temp = db['my_list']
    temp.append(5)
    db['my_list'] = temp

    daw = db['awesome']
    print(id(aw), id(daw))
    del db['awesome']


print('--------')

with shelve.open(filename) as states:
    for key in states:
        print(f'{key}: {states[key]}')
    print(states['my_list'])
    print(states['dummy'].default)


