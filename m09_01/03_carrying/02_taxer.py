def taxer_simple(base_tax, money):
    if money >= 10_000:
        base_tax = 1.5 * base_tax

    return money - base_tax * money


boris = taxer_simple(0.1, 6000)
andy = taxer_simple(0.1, 20_000)
print(boris, andy)



