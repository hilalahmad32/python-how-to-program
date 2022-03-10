import csv
from ntpath import join

with open(r"myFile0.csv") as csv_file:
    csv_read = csv.reader(csv_file, delimiter=",")
    counter = 0
    for row in csv_read:
        if counter == 0:
            print(f"Columen names is, {','.join(row)} ")
            counter += 1
        else:
            print(
                f"\n your id is {row[0]} , first name {row[1]} , lastname {row[2]}")
print("Process Complete")
