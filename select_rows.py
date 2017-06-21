#   execfile('select_rows.py')
import csv
count = -1
a = []
with open('CAR_PRICE_TIME_BW.csv') as infile:
	#reader = csv.DictReader(infile)
	#writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
	#writer.writeheader()
    #for i,row in enumerate(reader):
    #	count += 1
    #    if i % 3 == 0 :
    #        writer.writrow(row)
    #writer.writerows([x for i,x in enumerate(reader) if i % 3 == 0])
    for line in infile:
    	print line
    	a.append(line.strip())




with open('CAR_PRICE_TIME_BW_new.csv','w') as outfile:
	outfile.write(a)