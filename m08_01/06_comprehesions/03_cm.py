#  Set Comprehension
squares = set()

for i in range(20):
    squares.add(i**2)

print(squares)

sq = {i**2 for i in range(20)}
print(sq)
