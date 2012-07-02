import urllib2
import json
import csv

csvWriter = csv.writer(open('fb_birthdays.csv', 'wb'), delimiter=' ',quotechar=',', quoting=csv.QUOTE_ALL)


def get_friends():
  url = 'https://graph.facebook.com/64900833/friends?access_token=AAACEdEose0cBAMlddZCoOgLyKIT73BFQUkCHvU2Bl5QRHKs4e2UH31GlU9rqZBq59Utf4Ghl6KGywGFOUS3m7fLG8ZAn3kZD'
  resp = urllib2.urlopen(url).read()
  data = json.loads(resp.decode('utf-8'))
  return data['data']

def picture(id_friend):
  url = 'https://graph.facebook.com/'+ id_friend + '/picture?type=large'
  return urllib2.urlopen(url).read()

def download_pics(friends):
  for f in friends:
      url = 'https://graph.facebook.com/' + (f['id']) + '/?access_token=AAACEdEose0cBAMlddZCoOgLyKIT73BFQUkCHvU2Bl5QRHKs4e2UH31GlU9rqZBq59Utf4Ghl6KGywGFOUS3m7fLG8ZAn3kZD'
      resp = urllib2.urlopen(url).read()
      data = json.loads(resp.decode('latin-1'))
      try:
          
          bd = data['birthday']
          name = data['name']
          uid = str(data['id'])
      except KeyError:
          print "No Birthday provided"
      except UnicodeEncodeError:
          print('unicode ascii bullshit')
      else:
          try:
              print str(bd + "," + name + "," + uid)
              csvWriter.writerow([bd, name, uid])

          except UnicodeEncodeError:
              print ('cannot write name')
              csvWriter.writerow([bd, uid])

              




download_pics(get_friends())
