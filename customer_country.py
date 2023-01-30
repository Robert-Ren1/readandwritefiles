import csv
customer_file = open('customers.csv', 'r')
out_file = open("customer_country.csv", 'w')

reader = csv.reader(customer_file, delimiter=",")

next(reader)
out_file.write("FirstName"+','+'LastName'+','+'Country'+'\n')
for i in reader:
    out_file.write(i[1]+','+i[2]+','+i[4]+'\n')

customer_file.close()
out_file.close()
