import csv

FILENAME = 'users.csv'

users = [
    {'name': 'Николай', 'age': 22, 'gender': 'male'},
    {'name': 'Мария', 'age': 22, 'gender': 'female'},
    {'name': 'Назар', 'age': 22, 'gender': 'male'},
]

with open(FILENAME, 'w', encoding='utf-8', newline='') as f:
    columns = users[0].keys()
    writer = csv.DictWriter(f, delimiter=',', fieldnames=columns)
    writer.writeheader()
    for row in users:
        writer.writerow(row)


with open(FILENAME, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)

        for row in reader:
            print(row)
