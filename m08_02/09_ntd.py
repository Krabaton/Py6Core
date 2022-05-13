from collections import namedtuple

color_type = namedtuple('RGB', ['red', 'green', 'blue'])

cat = color_type(100, 20, 34)
rabbit = color_type(0, 234, 123)
print(cat)