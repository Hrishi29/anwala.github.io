import os
from boilerpipe.extract import Extractor

# creating directory using os library
os.mkdir("processed")


count = 1

while (count < 1001):
	with open('raw_html/%s.html' % count, 'r+', encoding='utf-8') as fp:
		#reading the collected html files from previous step 
		extractor = Extractor(extractor='ArticleExtractor', html=fp.read())
		#extracting non-html content
		processed = extractor.getText()
		with open('processed/%s.txt' % count, 'w', encoding='utf-8') as outfile1:
			outfile1.write(processed)

			
	count = count + 1
	