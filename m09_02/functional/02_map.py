# Map

names = ["dan", "jane", "steve", "mike"]


# 1
def normalize(name):
    return name.title()

new_name = []
for name in names:
    new_name.append(name.title())
print(new_name)


new_name = map(normalize, names)
print(list(new_name))

# 2

new_name = map(str.title, names)
print(list(new_name))

# 3

new_name = map(lambda name: name.title(), names)
print(list(new_name))


# 4
new_name = [name.title() for name in names]
print(list(new_name))