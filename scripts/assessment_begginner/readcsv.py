import csv
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
print(my_path)
path = os.path.join(my_path, "..../../python_sample.csv")
prv, prv1, prv2, max, max1, max2 = 0, 0, 0, 0, 0, 0

try:
    csv_reader = csv.reader(open(path), delimiter=',')
    next(csv_reader)

    for line in csv_reader:

        if int(line[2]) > int(prv):
            max = line[2]
            prv = line[2]

        if int(line[3]) > int(prv1):
            max1 = line[3]
            prv1 = line[3]

        if int(line[4]) > int(prv2):
            max2 = line[4]
            prv2 = line[4]
    print(max, max1, max2)

except FileNotFoundError as e:
    print("FileNotFoundError", e)
except Exception as e1:
    print("Something went wrong", e1)
