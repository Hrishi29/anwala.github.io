import json
from pprint import pprint
import csv
#with open('timemaps/1.json', 'w+') as outfile:
with open('previousMC.csv', 'a+', newline='') as csvfile:
	fieldnames = ['Memento_Count']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	csvfile.close()

for i in range(1,1001):
	try:	
		#loading json data if file is with .json extension
		json_file = 'timemaps/' + str(i) +'.json'
		json_data=open(json_file)
		data = json.load(json_data)
		#accesing the number of mementos by counting number of keys in list
		j = data['mementos']['list']
		#pprint(len(j))
		json_data.close()
		mementocount=len(j)
		json_data.close()
		with open('previousMC.csv', 'a+', newline='') as csvfile:
			fieldnames = ['Memento_Count']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writerow({'Memento_Count': mementocount})
			csvfile.close()
	except:
		mementocount=0
		# memento count is zero if file extension is txt
		with open('previousMC.csv', 'a+', newline='') as csvfile:
			fieldnames = ['Memento_Count']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writerow({'Memento_Count': mementocount})
			csvfile.close()
		pass

	#j = json.loads(outfile.read())
	#print (j[''])
	#outfile.close