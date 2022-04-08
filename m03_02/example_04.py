def real_cost(base, discont=0):
    return base * (1 - discont)


price_bread = 15
price_butter = 50
price_sugar = 60

current_price_bread = real_cost(price_bread)
current_price_butter = real_cost(price_butter, 0.05)
current_price_sugar = real_cost(price_sugar, 0.07)

print(f'New cost of bread {current_price_bread}')
print(f'New cost of butter {current_price_butter}')
print(f'New cost of sugar {current_price_sugar}')
