from urllib2 import urlopen
from json import loads
import json
 
accessToken = 'AAACgchb9wAUBAPVKmhZC5DZAqzEyyyt4y62tSalXOBrg0QDB5W2ONkRnbtoZCns2EK2bwZBGNDnbHvKp7yl1VYBRPVI9yD4ZD'  #INSERT YOUR ACCESS TOKEN
userId = '64900834'           #INSERT YOUR USER ID
 
# THIS IS KNOWN AS POSTS ON OPEN GRAPH

url='https://graph.facebook.com/' + userId + '/Statuses?limit=30&access_token=' + accessToken
jsonContent = loads(urlopen(url).read())
 

for item in jsonContent['data']:
    if 'story' in item:
        print 'STORY'
        print item['story']
        print '\n'

    elif 'message'in item:
        print 'MESSAGE'
        print item['message']
        if 'likes' in item:
            for i in item['likes']['data']:
                print (i['name'] + ", " + i['id'])
        else:
            print 'NO LIKES'
        print ('\n') 
    else:
        print  ('ERROR\n')

