my_set = {4, 6, "Oleg", "Python", 100}
my_set.add("Daria")
print("Daria" in my_set)

my_set.remove("Daria")
my_set.discard("Daria")  # нет ошибки при удалении не существующего элемента
