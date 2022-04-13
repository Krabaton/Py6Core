my_list = [1, 1, 2, 3, 5, 8, 13, 21, 7, 5, 100]

# print(my_list[4])
# print(len(my_list))
# for el in my_list:
#     print(el)

print(my_list)
# my_list.append(16)
# my_list.insert(6, -1)

# Удаляем все элементы 5

# for el in my_list:
#     if el == 5:
#         my_list.remove(el)

# while True:
#     if 5 in my_list:
#         my_list.remove(5)
#     else:
#         break
# -----------------------

# el = my_list.pop(4)
# print(el)
# new_list = [0, 31, 33, 27]
# my_list.extend(new_list)

# if 5 in my_list:
#     print(my_list.index(5))
# if 15 in my_list:
#     print(my_list.index(15))

# for _ in range(my_list.count(5)):
#     my_list.remove(5)
# print(my_list.count(5))

new_list = my_list.copy()

# sorted_list = sorted(my_list)
# print(sorted_list)

my_list.sort(reverse=True)
new_list.clear()

# print(my_list)
# print(new_list)

msl = ["Hello", "Hi", "Abc", "Aac", "Abb", "baz", "foo", "aaa"]
msl.sort()
print(msl)
