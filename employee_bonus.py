import csv
infile = open("EmployeePay.csv", 'r')

employee = csv.reader(infile)

for i in employee:
    print(*i, sep=", ")

infile.close()
