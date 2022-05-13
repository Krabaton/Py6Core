# Dict Comprehension

squares = {}

for i in range(20):
    squares[i] = i**2

print(squares)

sq = {i: i**2 for i in range(20)}
print(sq)
