# Методы __repr__ и __str__

class Car:
    store_name = 'Шина класна машина'

    def __init__(self, year, mark, model, color):
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color

    def __repr__(self):
        return f"Car({self.year}, '{self.mark}', '{self.model}', '{self.color}')"

    def __str__(self):
        return f"{self.store_name} - {self.mark}.{self.model}: {self.year}, {self.color}"


car = Car(2016, 'Zaz', 'Forza', 'White')
print(car)  # print(str(car))
print(repr(car))
# copy_car = eval(repr(car))
# print(copy_car.model)
