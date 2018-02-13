import requests
import json
import os
import csv

#directory for storing timemaps for each uri
os.mkdir("timemaps")
count = 1

#dictionary for sorting
dict={}
with open('1000ulinks.txt') as fp:
	for line in fp:
#get request made to memgatorin as json 
		url = 'http://memgator.cs.odu.edu/timemap/json/' + line.strip()
		
		
		try:
			req = requests.get(url, stream=True, headers={'User-Agent':'Mozilla/5.0'})
			resp = requests.head(url, stream=True, headers={'User-Agent':'Mozilla/5.0'})
		
		
		
			if req.status_code == 200 :
			
#dumping json data into respective timemap files for URI				
				with open('timemaps/%s.json' % count, 'w+') as outfile:
					json.dump(req.json(), outfile, sort_keys = True, indent = 4, ensure_ascii = False)
#getting mementocount					
					mementocount = resp.headers.get('X-Memento-Count')
#dictionary for sorting the number of mementos with	URIs				
					if mementocount in dict:
						dict[mementocount] += 1
					else: 
						dict[mementocount] = 1
						
					
#if 404 storing no mementos in for respective URI 				
			else :
				with open('timemaps/%s.txt' % count, 'w+') as outfile1:
					outfile1.write('No Momentos')
					mementocount = 0
					if mementocount in dict:
						dict[mementocount] += 1
					else: 
						dict[mementocount] = 1
					
			count = count + 1	
			
		
		except:
			pass
		
		
#Dumping data into csv file in Memento-Count and URI count columns		
with open('timemaps.csv', 'w', newline='') as csvfile:
	fieldnames = ['Memento_Count', 'URI_Count']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	
	for key, value in dict.items():
		writer.writerow({'Memento_Count': key, 'URI_Count': value})
	csvfile.close()