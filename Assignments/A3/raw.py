import requests 
import os



count = 1
#creating directory using os package
os.mkdir("raw_html")

with open('1000ulinks.txt') as fp:
	
	for line in fp:
	#getting the raw html for each of the 1000 URIs using requests
		try:
			req = requests.get(line.strip(), timeout=6, stream=True, headers={'User-Agent':'Mozilla/5.0'})
			string = req.text
			
		
	#writng the output as encoding 'utf-8'	
			with open('raw_html/%s.html' % count, 'w', encoding='utf-8') as outfile1:
				outfile1.write(string)
				outfile1.close()
			
			count = count + 1
		
		except:
			pass
		