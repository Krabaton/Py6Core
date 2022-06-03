# Инкапсуляция в Python (property, setter)

class Animal:
    def __init__(self, nickname, age, weight):
        self.__nickname = None
        self.__age = None
        self.__weight = None
        # Сеттеры срабатывают
        self.name = nickname
        self.age = age
        self.weight = weight

    @property
    def name(self):
        return self.__nickname

    @name.setter
    def name(self, nickname):
        if len(nickname) > 0:
            self.__nickname = nickname
        else:
            raise ValueError('Животные должны иметь имя!')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in list(range(0, 50)):
            self.__age = age
        else:
            raise ValueError('Животные столько не живут!')

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError('Животные должны, что-то весить!')


chup = Animal('Chupakabra', 12, 100)
print(chup.name, chup.age, chup.weight)
print(chup._Animal__nickname)

print('---------------------')
try:
    t_chup = Animal('Chupakabra', -3, 100)
    print(t_chup.name, t_chup.age, t_chup.weight)
    t_chup.weight = -5
except ValueError as err:
    print(err)