from linkedin import linkedin

API_KEY = '86kugk5q9awmxj'
API_SECRET = 'CUZoPYntqc3SEcRP'
RETURN_URL = 'http://www.cs.odu.edu/~anwala/'

authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL)
# Optionally one can send custom "state" value that will be returned from OAuth server
# It can be used to track your user state or something else (it's up to you)
# Be aware that this value is sent to OAuth server AS IS - make sure to encode or hash it
#authorization.state = 'your_encoded_message'
authentication.authorization_url  # open this url on your browser
#Authentication
application = linkedin.LinkedInApplication(authentication)
authentication.authorization_code = 'AQQWMhrgDvMWS8zAKr4uApwt81fFqqvJA1ioRxnbA1JMuKTaJYdrtnV2-AUfSt8a_xI9AME14ewCrcGowNRwSLQaQXoP-kzzC3eaa-wTHcMk0ylezMLZSjZFIVN7YNLn04547B6Jl4UFfQbk-uiLTNZAtPWTIg'
#get access token
authentication.get_access_token()

#set access token
application = linkedin.LinkedInApplication(token=authentication.get_access_token())
#accessing basic profile api
print(application.get_profile(selectors=['num-connections']))
#accessing connections api
print(application.get_connections())
#accessing search profile api
print(application.search_profile(selectors=[{'people': ['first-name', 'last-name']}], params={'keywords': 'apple microsoft'}))
