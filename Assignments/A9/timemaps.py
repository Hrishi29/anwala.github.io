import requests
import json
import os
import csv

#directory for storing timemaps for each uri
os.mkdir("timemaps")
count = 1

with open('counting.csv', 'a+', newline='') as csvfile:
	fieldnames = ['Memento_Count']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	csvfile.close()
with open('1000_links.txt') as fp:
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
					with open('counting.csv', 'a+', newline='') as csvfile:
						fieldnames = ['Memento_Count']
						writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
						writer.writerow({'Memento_Count': mementocount})
						csvfile.close()

						
					
#if 404 storing no mementos in for respective URI 				
			else :
				with open('timemaps/%s.txt' % count, 'w+') as outfile1:
					outfile1.write('No Momentos')
					mementocount = 0
					with open('counting.csv', 'a+', newline='') as csvfile:
						fieldnames = ['Memento_Count']
						writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
						writer.writerow({'Memento_Count': mementocount})
						csvfile.close()

			count = count + 1	
			
		
		except:
			with open('timemaps/%s.txt' % count, 'w+') as outfile1:
					outfile1.write('No Momentos')
					mementocount = 0
					with open('counting.csv', 'a+', newline='') as csvfile:
						fieldnames = ['Memento_Count']
						writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
						writer.writerow({'Memento_Count': mementocount})
						csvfile.close()
			count = count + 1
			pass
		
		
