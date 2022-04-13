list1 = [1, 2, 3, 4, 55, 13, 21, 100]
list2 = [2, 2, 2, 33, 3, 3, 5, 4]

set1 = set(list1)
set2 = set(list2)
print(set1, set2)

set_union = set1 | set2  # объединение
print(list(set_union))

set_cross = set1 & set2  # пресечение
print(list(set_cross))
