import csv

with open("users.csv", "r") as users:
    reader = csv.DictReader(users)
    for row in reader:
        print(row["Name"] + " is " + row["Age"] + " years old and is a " + row["Gender"] + ".")