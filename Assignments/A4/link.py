from linkedin import linkedin
from urllib.parse import urlparse, parse_qs
import requests
API_KEY = '86kugk5q9awmxj'
API_SECRET = 'CUZoPYntqc3SEcRP'
RETURN_URL = 'http://www.cs.odu.edu/~anwala/'

#authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL)
# Optionally one can send custom "state" value that will be returned from OAuth server
# It can be used to track your user state or something else (it's up to you)
# Be aware that this value is sent to OAuth server AS IS - make sure to encode or hash it
#authorization.state = 'your_encoded_message'
#print(authentication.authorization_url)  # open this url on your browser

#application = linkedin.LinkedInApplication(authentication)
#authentication.authorization_code = 'AQQWMhrgDvMWS8zAKr4uApwt81fFqqvJA1ioRxnbA1JMuKTaJYdrtnV2-AUfSt8a_xI9AME14ewCrcGowNRwSLQaQXoP-kzzC3eaa-wTHcMk0ylezMLZSjZFIVN7YNLn04547B6Jl4UFfQbk-uiLTNZAtPWTIg'
#print(authentication.get_access_token())

application = linkedin.LinkedInApplication(token='AQUf73tCwglMAaeBYu75AELR68mvKR53QXgQXSAluSn3lgoe_HBOOva3bK7SCNVZiGM-J3iDj1hIt-0dQejvXHxdlwXdtNlDqPMh2H4EoNHBWxkuYlsSRSE52uam-bQdthAhlymBQ2BuURP4RFCF7CEhzUdd16nAWV-HJs2pJmr-ztBUqxFy8SViAUW1XcB_bU8WqzVmBemWle8TNeu1hMUR5kBkGTIMeFJzanPBdUUtOGEFWLGNrd0pRRmgC6eMhQWOahDxZX0OTOowmXnnLCclYscT3daWoFCDfNVuRuwuQqA4eIi64K2H0C9tnMXUmKz7LvVsNTM-XhXbryVK7HwEaSAzIg')
#http://www.cs.odu.edu/~anwala/?code=AQT2MopqRhtdyvTWNGZx6WTSch5RjM_cJFH56Za143FhaM4vQOMP2gxzF3Xon-eB6CFQnFNsWS1e4QyXA1pB5j8xGyK8VCrD5BZ8fydhj41T7OrEqkhlHmLTu1VufC1yw27DjjYAGqzHtUd-O3u2tJwonFdhmg&state=4517cc29f3daa970751ba4de26682552#!
print(application.get_profile(selectors=['num-connections']))
print(application.get_connections())
print(application.search_profile(selectors=[{'people': ['first-name', 'last-name']}], params={'keywords': 'apple microsoft'}))
