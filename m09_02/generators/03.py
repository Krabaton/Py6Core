# Свой генератор range

def my_range(limit):
    value = 0
    while value < limit:
        yield value
        value = value + 1


# for num in range(5):
#     print(num)

# for num in my_range(5):
#     print(num)

gen = my_range(5)

while True:
    try:
        r = next(gen)
        print(r)
    except StopIteration:
        break

print('The end')

