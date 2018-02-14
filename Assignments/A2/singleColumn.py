import csv

with open('counts.csv', 'a+', newline='') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow('Memento_Count')
	csvfile.close()
#reading rows from csv file		
with open('names.csv', newline='') as csvfile:
	field = ['Memento_Count', 'URI_Count']
	reader = csv.DictReader(csvfile, fieldnames=field)
	for row in reader: 
		if row['URI_Count'] == "URI_Count":
			continue 	
		count = row['URI_Count']
		count = int(count)
#storing all the mementos in single column based on their counts		
		for row1 in range(0,count):
			
			with open('counts.csv', 'a+', newline='') as csvfile:
				spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
				spamwriter.writerow(row['Memento_Count'])
				csvfile.close()
	