import requests
import json
from datetime import datetime
import csv


#counts initialized

count = 1
count_nocd = 0
count_nomem = 0

#write first row as headers in csv file		
with open('dates.csv', 'a+', newline='') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|')
	spamwriter.writerow(['Age','Memento-Count'])
	csvfile.close()
						
with open('1000ulinks.txt') as fp:
	for line in fp:
		try:
#requests made to memgator as well as carbon date url 		
			urlmem = 'http://memgator.cs.odu.edu/timemap/json/' + line.strip()
			urlcd = 'http://cd.cs.odu.edu/cd/' + line.strip()
			reqmem = requests.head(urlmem, stream=True, headers={'User-Agent':'Mozilla/5.0'})
			
#if no mementos 		
			if reqmem.status_code == 404:
				reqcd = requests.get(urlcd, stream=True, headers={'User-Agent':'Mozilla/5.0'})
				data = reqcd.json()
#get the count for no date estimates if any			
				if data['estimated-creation-date'] == "":
					count_nocd = count_nocd + 1
					count_nomem = count_nomem +1
					
				else:
					count_nomem = count_nomem +1
			
			
			
			else:
				reqcd = requests.get(urlcd, stream=True, headers={'User-Agent':'Mozilla/5.0'})
				data = reqcd.json()
#check if any uri having memento count has no estimate date creation
				if data['estimated-creation-date'] == "":
					count_nocd = count_nocd + 1
#else get the age in days using datetime					
				else:
					memento_count = reqmem.headers.get('X-Memento-Count')
					birthday = data['estimated-creation-date']
					birthday = datetime.strptime(birthday, '%Y-%m-%dT%X')
					age = datetime.now() - birthday
#dump data into csv file					
					with open('dates.csv', 'a+', newline='') as csvfile:
						spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|')
						spamwriter.writerow([age.days, memento_count])					
						csvfile.close()
					
#the other data required dumped in calc.csv file		
			with open('calc.csv', 'w', newline='') as csvfile:
				spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|')
				spamwriter.writerow(['Total URIs','No Mementos','No Date Estimate'])
				spamwriter.writerow(['1000',count_nomem,count_nocd])	
				csvfile.close()
		
			
		
		except:
			pass
