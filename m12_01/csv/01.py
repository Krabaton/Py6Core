import csv

with open('names.csv', 'w', encoding='utf-8', newline='') as f:
    fields_name = ['first_name', 'last_name']
    writer = csv.DictWriter(f, fieldnames=fields_name)
    writer.writeheader()
    writer.writerow({'first_name': 'Anastasia', 'last_name': 'Ivanitskaya'})
    writer.writerow({'first_name': 'Yurii', 'last_name': 'Kuchma'})
    writer.writerow({'first_name': 'Michail', 'last_name': 'Kravchenko'})

with open('names.csv', 'r', encoding='utf-8') as f:
    data = f.read()
    print(data)