list_daria = ["Red", "Green", "Black", "White"]
list_oleg = ["Red", "White", "Black", "Yellow"]

list_only_daria = list(set(list_daria) - set(list_oleg))
print(list_only_daria)


list_u = list(set(list_daria) ^ set(list_oleg))
print(list_u)
