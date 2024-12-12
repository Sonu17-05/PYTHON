import csv

field_name = ['no', 'company', 'car model']
car = [
    {'no': 1, 'company': 'ferrari', 'car model': 'GH'},
    {'no': 2, 'company': 'bmw', 'car model': 'x5'},
    {'no': 3, 'company': 'mercedes', 'car model': 'benz'},
    {'no': 4, 'company': 'honda', 'car model': 'nsx'},
    {'no': 5, 'company': 'pagani', 'car model': 'zonda'}
]


with open('car.csv', 'w', newline='') as csvfile:
    write = csv.DictWriter(csvfile, fieldnames=field_name)
    write.writeheader()
    write.writerows(car)


with open('car.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for r in reader:
        print(', '.join([f"{key}: {value}" for key, value in r.items()]))
