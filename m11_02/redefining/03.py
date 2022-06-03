# Логические операции

class Car:
    store_name = 'Шина класна машина'

    def __init__(self, year, mark, model, color, price):
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color
        self.price = price

    def __repr__(self):
        return f"Car({self.year}, '{self.mark}', '{self.model}', '{self.color}', '{self.price}')"

    def __str__(self):
        return f"{self.store_name} - {self.mark}.{self.model}: {self.year}, {self.color}, '{self.price}'"

    def __eq__(self, other):
        return self.price == other.price

    def __ne__(self, other):
        return self.price != other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price


car_w = Car(2016, 'Zaz', 'Forza', 'White', 5500)
car_b = Car(2017, 'Zaz', 'Forza', 'Black', 6500)

print(car_w == car_b)
print(car_w > car_b)
print(car_w < car_b)
print(car_w >= car_b)
print(car_w <= car_b)
