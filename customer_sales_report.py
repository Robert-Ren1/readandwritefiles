import csv
infile = open('sales.csv', 'r')
outfile = open("salesreport.csv", 'w')

read = csv.reader(infile, delimiter=',')

next(read)
outfile.write('CustomerID'+', ' + "calculated total" + '\n')
for i in read:
    total = (float(i[3])+float(i[4])+float(i[5]))
    total = str(total)
    outfile.write(i[0]+', '+total+"\n")

outfile.close()
