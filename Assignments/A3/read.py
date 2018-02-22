import justext
import re

para = ''
d = {}
inv = []
count = 1

while (count < 1001):
	with open('raw_html/%s.html' % count, 'r', encoding='utf-8') as fp:
		#reading the files for raw html content
		wordstring = fp.read()
		#extracting linguistic sentences from the content by excluding the boilerplate content
		paragraphs = justext.justext(wordstring, justext.get_stoplist("English"))
		for paragraph in paragraphs:
		
			if not paragraph.is_boilerplate:
				para = para + ' ' + (paragraph.text)
		#creating a list of words
		wordlist = para.split()
	
		for w in wordlist:
		#excluding non-alphanumeric characters
			w = re.sub(r'\W+', '', w) 
		
		#checkig for duplicates
			if w not in inv:
			# check if string not empty	
				if w:  
					inv.append(w)
				
		for w1 in inv:
			#appending values to keys in dictionary		
			try:		
				d[w1].append(count)
			except KeyError:
				d[w1] = [count]
				pass
	count = count + 1
	#writing the result in invertedindex.txt file in ascii format
with open('invertedindex.txt', 'w', encoding='ascii') as pp:
		for k, v in d.items():
			pp.write(str(k) + ' >>> '+ str(v) + '\n\n')
