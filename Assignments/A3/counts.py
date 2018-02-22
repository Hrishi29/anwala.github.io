import math
import os
import csv
import linecache

# getting the curent directory path and appending to the queried_docs folder
path = os.getcwd() + '/queried_docs'
counts = 1
tuple = []
#Reading the files one by one from the directory containing 10 URIs
for filename in os.listdir(path):
	with open('queried_docs/%s' % filename, 'r', encoding='utf-8') as fp:
		wordstring = fp.read()
		#creating list of words
		wordlist = wordstring.split()
		#calculating TF, IDF, TFIDF values for each document
		TF = (wordlist.count('football'))/(len(wordlist))
		DF = 47000000000/1470000000
		IDF = math.log(DF,2)
		TFIDF = TF*IDF
		list = os.path.splitext(os.path.basename(filename))
		#getting the URI from the links files based on the line number and document number
		linecount = int(list[0])
		r = linecache.getline('1000ulinks.txt', linecount)
		URI = r.strip()
		tuple = tuple + [(TFIDF, TF, IDF, URI),]
		fp.close()
#sorting the tuple based on TFIDF value in descending order
tuple = sorted(tuple, key=lambda tuples:tuples[0], reverse=True )	

#writing the output in csv file
with open('rank.csv', 'a+', newline='') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|')
	spamwriter.writerow(['TF-IDF', 'TF', 'IDF', 'URI'])
	for a,b,c,d in tuple:
	
	
		spamwriter.writerow(['%.3f' % a,'%.3f' % b,'%.3f' % c, '%s' % d])
	

	csvfile.close()
	