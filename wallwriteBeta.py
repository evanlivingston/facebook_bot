import urllib

def write(userID, message):

    params = {}

    params['access_token'] = 'AAACEdEose0cBAMlddZCoOgLyKIT73BFQUkCHvU2Bl5QRHKs4e2UH31GlU9rqZBq59Utf4Ghl6KGywGFOUS3m7fLG8ZAn3kZD'
    params['message'] = message

    params = urllib.urlencode(params)
    f = urllib.urlopen("https://graph.facebook.com/"+userID+'/feed?', params)
    print f.read()
