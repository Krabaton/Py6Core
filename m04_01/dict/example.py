grade1 = {"Oleg": 2, "Alexx": 3}
grade2 = {"Nastya": 5, "Sergey": 4}
grade3 = {"Alex": 4, "Andry": 5}

result = {}

for d in (grade1, grade2, grade3):
    result.update(d)

print(result)
