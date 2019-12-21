import csv

with open('csv.csv') as csv_file:
	csv_reader = csv.reader(csv_file)

	for line in csv_reader:
		print(line)

# o/p:
# ['first_name', ' last_name', ' location']
# ['Sandeep', ' Tiwari', ' Noida']