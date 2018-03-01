import requests
import tweepy
from tweepy import OAuthHandler
import csv

#get keys from: https://apps.twitter.com/
#consumer key, consumer secret, access token, access secret.
ckey = 'bSeaweiw68Hma0VLyeEd9se9u'
csecret = 'jch6kXwJociEynIHDoC8OunYLsYeRDCCjkaz0EUf3CSHzrNpSd'
atoken = '958819771000205312-w7L1GrIudQbONzjpfMRbwD33ITfWxnB'
asecret = 'MKE2Au1XVZDg1xV1F4USZsuIETm7WxgEuLACbDiQooxHG'

# csv file open to write headers
with open('followers.csv', 'a+', newline='') as csvfile:
	fieldnames = ['Users', 'FollowersCount']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
csvfile.close()

#OAuth authorization		
auth = OAuthHandler(ckey, csecret)

auth.set_access_token(atoken, asecret)
#getting api access
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60)

users=[]

#accessing followers api
for user in tweepy.Cursor(api.followers, screen_name='acnwala', count=200).pages():
	users.extend(user)
	for i in users:
		count = i.followers_count
		foll=i.screen_name
#writing output to csvfile		
		with open('followers.csv', 'a+', newline='') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writerow({'Users': foll, 'FollowersCount': count})
			csvfile.close()
		
	




		