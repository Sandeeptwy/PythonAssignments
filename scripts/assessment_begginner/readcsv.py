import csv

path = "D:\\3Pillar\\Python\\Assignment\\python_sample.csv"
csv_reader = csv.reader(open(path), delimiter=',')

prv, prv1, prv2, max, max1, max2 = 0, 0, 0, 0, 0, 0

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