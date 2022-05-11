import math

x = float(input('x='))
y = float(input('y='))

a = math.log(math.pow(y, -math.sqrt(math.fabs(x)))) * \
    (math.sin(x) + math.exp(x + y))

print(a)
