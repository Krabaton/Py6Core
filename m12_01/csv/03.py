import csv

country_codes = {}

with open('countries.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:
        country_codes[line[0]] = line[1]

print(country_codes)
print(country_codes['UA'])