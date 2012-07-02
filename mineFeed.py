from urllib2 import urlopen
from json import loads
import json
 
accessToken = 'AAACgchb9wAUBAPVKmhZC5DZAqzEyyyt4y62tSalXOBrg0QDB5W2ONkRnbtoZCns2EK2bwZBGNDnbHvKp7yl1VYBRPVI9yD4ZD'  #INSERT YOUR ACCESS TOKEN
userId = '64900834'           #INSERT YOUR USER ID
 
# Read my likes as a json object
url='https://graph.facebook.com/' + userId + '/feed?limit=30&access_token=' + accessToken
jsonContent = loads(urlopen(url).read())
 

for item in jsonContent['data']:
    if 'story' in item:
        print 'STORY'
        print item['story']
        print '\n'

    elif 'message'in item:
        print 'MESSAGE'
        print item['message']
        if 'discription' in item:
            print item['description']
        else:
            print 'NO DISCRIPTION'
            print item['type']
        print ('\n') 
    else:
        print  ('ERROR\n')

