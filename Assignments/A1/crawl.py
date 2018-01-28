#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import sys
import urllib
from urllib.parse import urlparse, urljoin

#Part 1 : Read in command line arguments
if len (sys.argv) == 2 :
	weblink = sys.argv[1]

else :
	print ("Usage:python crawl.py url")
	sys.exit (1)	

# Request data using get
try :
	urllib.request.urlopen(weblink)
	responsedurl = requests.get(weblink)
	
#get http response
#if multiple-redirection exists get new URI	
	if responsedurl.history :
		print ("Request was redirected to new link")
		print ("New Link: " + responsedurl.url)
		response = requests.get(responsedurl.url)
		data = response.text
	
	else :
		response = requests.get(weblink)
		data = response.text

except :
	print ("Enter a valid url")
	sys.exit (1)

#Extract all links from the webpage using BeautifulSoup 
soup = BeautifulSoup(data, 'lxml')
print ("Extracting all links from webpage:\n")
for link in soup.findAll('a', href=True):
	webb = link.get('href')
	print (webb)

#Extract all pdf links from the webpage if present	
print ("\nExtracting pdf links from webpage if present:\n")	
for pdflinks in soup.findAll('a', href=True):
	web = pdflinks.get('href')

#check if any relative links present	
	if bool(urlparse(web).netloc) == False :
		web = urljoin(weblink, web)
		
		
	try:
		urllib.request.urlopen(web)
		req = requests.get(web)
		resp = requests.head(web)

#return pdf links with status_code 200		
		if req.status_code == 200 and resp.headers.get('content-type') is not None :
		
			if "application/pdf" in resp.headers['content-type'] :
				print ("First Link: " + web)
				print ("Final Link: " + web)
				print("Bytes: " + resp.headers['content-length'] + '\n')

#return pdf links for the final URI if any redirects				
		if req.history:
			final = req.url
			finalresp = requests.head(final)
			if finalresp.headers.get('content-type') is not None :
				if "application/pdf" in finalresp.headers['content-type'] :
					print ("Request was redirected")
					print ("First Link: " + web)
					print ("Final Link: " + final)
					print("Bytes: " + finalresp.headers['content-length'] + '\n')
		
	except:
		pass
	