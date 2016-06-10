from bs4 import BeautifulSoup
import urllib2
import urllib
import json

def download_one_song(code):
    '''
    downloads one song and return the result as a json string
    '''
    f_code = str(code)

    data = urllib.urlencode({'toneId': fcode })
    url = "http://rbt.irancell.ir/user/qryListenUrlById.screen"

    r = urllib2.Request(url=url,data=data)
    response = urllib2.urlopen(r)
    j_response = json.loads(response.read().strip())

    name = j_response["toneInfo"]["toneName"]
    price = j_response["toneInfo"]["price"]
    singer_name = j_response["toneInfo"]["singerName"]
    tone_valid_day = j_response["toneInfo"]["toneValidDay"]
    audio_link = j_response["toneInfo"]["tonePreListenAddress"]
    tone_id = j_response["toneInfo"]["toneID"]
    tone_code = j_response["toneInfo"]["toneCode"]

    album = ?
    category = ?
