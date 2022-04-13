import sys

print(sys.argv)

for arg in sys.argv:
    print(arg)

person = {"name": sys.argv[1], "age": sys.argv[2], "lang": sys.argv[3]}
print(person)
