import re

count = 1

while (count < 1001):
	with open('processed/%s.txt' % count, 'r+', encoding='utf-8') as fp:
	#reading the conent from processed folder containing processed documents
		content=fp.read()
	#searching the documents for query football	
		if re.search('football', content):
	#storing the documents containing the query in queried_docs folder	
			with open('queried_docs/%s.txt' % count, 'w', encoding='utf-8') as fp1:	
				fp1.write(content)
		
					
	count = count + 1
	