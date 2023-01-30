import csv
infile = open('sales.csv', 'r')
outfile = open("salesreport.csv", 'w')

read = csv.reader(infile, delimiter=',')
next(read)
outfile.write('CustomerID'+' | ' + "Total" + '\n')
value = 250
total = 0
for i in read:
    if int(i[0]) == value:
        total = (total + float(i[3])+float(i[4])+float(i[5]))
    elif int(i[0]) != value:
        result = "{:.2f}".format(total)
        outfile.write("       "+str(value) + '   ' + str(result)+'\n')
        value += 1
        total = 0
        total += float(i[3])+float(i[4])+float(i[5])

try:
    next(read)
except StopIteration:
    result = "{:.2f}".format(total)
    outfile.write("       "+str(value) + '   ' + str(result)+'\n')


outfile.close()
