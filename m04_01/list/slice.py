my_string = "Hello my little friends!"
my_list = [1, 1, 2, 3, 5, 8, 13, 21, 7, 5, 100]

print(my_list[:5:2])
print(my_string[0:5:2])
print(my_list[6:])
print(my_list[6::-1])

new_list = my_list[:]  # копирование списка
reversed_copy_list = my_list[::-1]  # развернуть список и скопировать

print(reversed_copy_list)
