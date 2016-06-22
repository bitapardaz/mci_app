import json
import urllib2,urllib
from urllib2 import HTTPError



def download_json(code):

    valid_json = False
    valid_code = False
    f_code = str(code)

    data = urllib.urlencode({'toneId': f_code })
    url = "http://rbt.irancell.ir/user/qryListenUrlById.screen"

    r = urllib2.Request(url=url,data=data)
    response = urllib2.urlopen(r)
    j_response = json.loads(response.read().strip())

    '''
    check if the json is empty.
    '''
    tone_info = j_response['toneInfo']
    if tone_info != None:
        '''
        the json has some information in it, but now we should check
        if the information is valid -- the audio link actually works
        '''
        audio_link = j_response["toneInfo"]["tonePreListenAddress"]
        r = urllib2.Request(url=audio_link)
        try:
            response = urllib2.urlopen(r)
            is_code_valid = True
            return True
        except HTTPError:
            is_code_valid = False
            return False
            name = ""
            price = ""
            return (is_song_valid,name,price)
    else:
        '''
        the json is empty: toneInfo:null
        '''
        return False
