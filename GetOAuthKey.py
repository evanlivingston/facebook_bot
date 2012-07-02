#!/usr/bin/python
# coding: utf-8
# Outputs an OAUTH token

import facebook
import urllib
import urlparse
import subprocess
import warnings

# Hide deprecation warnings. The facebook module isn't that up-to-date (facebook.GraphAPIError).
warnings.filterwarnings('ignore', category=DeprecationWarning)

# Parameters of your app and the id of the profile you want to mess with.
FACEBOOK_APP_ID     = '176411872444421'
FACEBOOK_APP_SECRET = '0c919b23dc224e94d0fb1567f6999f90'
FACEBOOK_PROFILE_ID = '64900833'

# Trying to get an access token. Very awkward.
oauth_args = dict(client_id     = FACEBOOK_APP_ID,
                  client_secret = FACEBOOK_APP_SECRET,
                  grant_type    = 'client_credentials')
oauth_curl_cmd = ['curl',
                  'https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(oauth_args)]
oauth_response = subprocess.Popen(oauth_curl_cmd,
                                  stdout = subprocess.PIPE,
                                  stderr = subprocess.PIPE).communicate()[0]

try:
    oauth_access_token = 'AAACgchb9wAUBAPVKmhZC5DZAqzEyyyt4y62tSalXOBrg0QDB5W2ONkRnbtoZCns2EK2bwZBGNDnbHvKp7yl1VYBRPVI9yD4ZD'
except KeyError:
    print('Unable to grab an access token!')
    exit()

facebook_graph = facebook.GraphAPI(oauth_access_token)

# Try to post something on the wall.
try:
    
    profile = get_object("me")
    print(profile)

except facebook.GraphAPIError as e:
    print 'Something went wrong:', e.type, e.message
