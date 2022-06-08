import csv

filename = 'table.csv'

with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    for i in range(1, 21):
        writer.writerow([i, i**2, i**3])

with open(filename, 'r', newline='') as f:
    reader = csv.reader(f)
    res = []
    for line in reader:
        res.append(line)

print(res)