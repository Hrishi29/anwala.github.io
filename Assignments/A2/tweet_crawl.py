#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import requests
import urllib
import tldextract
from urllib.parse import urlparse, urljoin
import sys

#get keys from: https://apps.twitter.com/
#consumer key, consumer secret, access token, access secret.
ckey = 'bSeaweiw68Hma0VLyeEd9se9u'
csecret = 'jch6kXwJociEynIHDoC8OunYLsYeRDCCjkaz0EUf3CSHzrNpSd'
atoken = '958819771000205312-w7L1GrIudQbONzjpfMRbwD33ITfWxnB'
asecret = 'MKE2Au1XVZDg1xV1F4USZsuIETm7WxgEuLACbDiQooxHG'
#created two blank lists for comparison 
links1 = []
links2 = []

#listen to the stream of data from twitter streaming API
class listener(StreamListener):

	def on_data(self, data):
		
#data in JSON format is extracted
		tweetJson = json.loads(data)
		
		
#get links from tweets 		
		links = tweetJson['entities']['urls']

#constraints set		
		if( len(links) != 0 and tweetJson['truncated'] == False ):
			
#links passed as dictionary		
			self.getLinksFromTweet(links)
				
		return True

	def getLinksFromTweet(self, linksDict):

		for uri in linksDict:
#establish http connection for head and get request			
			urllib.request.urlopen(uri['expanded_url'])
			req = requests.get(uri['expanded_url'])
			resp = requests.head(uri['expanded_url'])
				

		
			if req.status_code == 200 and resp.headers.get('content-type') is not None :
#check if expanded_url has any redirections or short links				
				if req.history:
					final2 = req.url
#extract domain name using tlde					
					extracted2 = tldextract.extract(final2)
					if extracted2.domain != 'twitter':
						o = urlparse(final2)
#separate uri path and query
						final3 = urljoin(final2, o.path)
						finalresp = requests.head(final3)
#make comparison and then append						
						if final3 not in links1:
							links1.append(final3)
							links2.append(final2)
							print(final2)
#similar steps for expanded_url							
				else:
					extracted3 = tldextract.extract(uri['expanded_url'])
					if extracted3.domain != 'twitter':
						o = urlparse(uri['expanded_url'])
						urilink = urljoin(uri['expanded_url'], o.path)
						if urilink not in links1:
							links1.append( urilink )
							links2.append( uri['expanded_url'] )
							print(uri['expanded_url'])
				
			if req.history:
				final = req.url
				extracted = tldextract.extract(final)
				if extracted.domain != 'twitter':
					o1 = urlparse(final)
					final4 = urljoin(final, o1.path)
					finalresp = requests.head(final4)
					
					if final4 not in links1:
						links1.append(final4)
						links2.append(final)
						print(final)
						
							
	
		
			

		return True

	def on_error(self, status):
		print( status )
		
		if status_code == 420:
#returning False in on_data disconnects the stream
			return False
		return True

		
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

#for getting just 1000 links
while len(links2) < 1001:
	try:
		twitterStream = Stream(auth, listener())
#multiple keywords used		
		twitterStream.filter(track=['trump', 'football', 'olympics', 'jenner', 'kardashian', 'politics'])

	except KeyboardInterrupt:	
		print()
		sys.exit (1)
	except:
		pass
