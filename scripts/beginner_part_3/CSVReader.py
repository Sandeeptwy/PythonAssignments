import csv

try:
    with open('csv.csv') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            print(line)
except Exception as e:
    print("FileNotFoundError", e)
except Exception as e1:
    print("Something went wrong", e1)
# o/p:
# ['first_name', ' last_name', ' location']
# ['Sandeep', ' Tiwari', ' Noida']
