sum = 0

for i in range(1, 3):
    print("---")
    for _el in range(1, 26):
        if sum >= 100:
            break
        sum += 5
    print(i)

print(sum)
