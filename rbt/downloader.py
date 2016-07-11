from bs4 import BeautifulSoup
import urllib2,urllib
from models import Song, Category, Producer, Album
import requests
import ssl
from functools import wraps

#################################################
### running the downloader
#################################################

def run_downloader(start_page,end_page):

    # on the website, the selector has the range (1,...,5700)
    # however, the urls are sent to an index page_number-1
    start_page = start_page - 1
    end_page = end_page - 1

    all_codes_string = get_all_valid_codes(start_page,end_page)
    all_codes_int = [ int(code_string) for code_string in all_codes_string]

    db_tones = Song.objects.values_list('activation_code',flat=True)

    new_tones = [ tone for tone in all_codes_int if tone not in db_tones]
    #excess_tones = [tone for tone in db_tones if tone not in all_codes_int]

    print "new tones = %d" % len(new_tones)
    #print "excess tones = %d" % len(excess_tones)

    command = input("Press 1 to continue: ")
    if command == 1:
        print "yeay"
    elif command ==2:
        print new_tones
        return None
    else:
        print "Nay"
        return None


    for id in new_tones:

        print("\n%s" % id),

        html_page = download_song_html(id)
        if is_song_valid(html_page):

            # get the information from mci site
            (code,name,producer_farsi,album_farsi,category_farsi) = derive_song_information(html_page)

            # check if the song already exists in the database
            try:
                song = Song.objects.get(activation_code=int(code))
                # the song already exists in the database.
                # Do nothing.
                print "- already exists"
            except Song.DoesNotExist:
                add_song_to_db(code,name,producer_farsi,album_farsi,category_farsi)
                print( "- inserted.")


    for id in excess_tones:

        song = Song.objects.get(activation_code=id)
        #song.delete()
        print "EXCESS SONG: activation code: %s" % song.activation_code


    print "Number of newly added songs: %d" % len(new_tones)
    # removing excess_tones
    print "Number of songs in excess: %d" % len(excess_tones)


def derive_song_information(html_page):

    soup = BeautifulSoup(html_page,'html.parser')
    table_tag = soup.table

    code = table_tag.find_all('td')[1].string.strip()
    name = table_tag.find_all('td')[3].string.strip()
    producer_farsi = table_tag.find_all('td')[5].string.strip()
    album_farsi = table_tag.find_all('td')[13].string.strip()
    category_farsi = table_tag.find_all('td')[17].string.strip()

    return (code,name,producer_farsi,album_farsi,category_farsi)

def is_song_valid(html_page):
    '''
    analyses the html response and check if the song is a valid one.
    '''
    soup = BeautifulSoup(html_page,'html.parser')
    audio= soup.find_all('audio')
    if not audio:
        return False
    else:
        return True


def download_song_html(id):
    """
    downloads the html file that is associated with the given id.
    """

    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    link = "http://rbt.mci.ir/AJAX/listen.jsp?toneID=%d" % id
    headers = { 'User-Agent' : user_agent }
    r = urllib2.Request(link, headers=headers)
    downloaded = urllib2.urlopen(r)
    html_page = downloaded.read()

    return html_page

def add_song_to_db(code,name,producer_farsi,album_farsi,category_farsi):

    # get or create producer
    try:
        producer,created = Producer.objects.get_or_create(name=producer_farsi)

    except Producer.MultipleObjectsReturned:
        producer = Producer.objects.filter(name=producer_farsi)[0]


    # get or create cateogory
    category,created = Category.objects.get_or_create(farsi_name=category_farsi)

    # get or create the album
    album,created = Album.objects.get_or_create(farsi_name=album_farsi,category=category)


    # audio download link
    audio_link = "http://rbt.mci.ir/wave/%s.wav" % code

    # save the song
    song = Song(activation_code=code,
                download_link=audio_link,
                song_name=name,
                producer=producer,
                album = album,
                confirmed = False,
                )
    song.save()



def get_all_valid_codes(start_page,end_page):
    '''
    returns the codes that corresponds to the valid songs on rbt.mci.ir
    '''

    all_codes = []
    for page in range(start_page,end_page):
        print "page %d" % page
        new_codes = get_valid_codes(page)
        all_codes = all_codes + new_codes
    return all_codes



def get_valid_codes(page):
    '''
    returns the list of valid codes defined in one page
    '''
    response = get_html_song_table(page)
    soup = BeautifulSoup(response.content,'html.parser')
    all_rows = soup.find_all('tr')
    valid_rows = filter_rows(all_rows)
    page_codes = []
    for row in valid_rows:
        code_string = row.find_all('td')[0].string.strip()
        page_codes = page_codes + [code_string]
    return page_codes



def filter_rows(all_rows):
    valid_rows = []
    for row in all_rows:
        if row['class'] == [u'even'] or row['class']==[u'odd']:
            valid_rows = valid_rows + [row]
    return valid_rows



def get_html_song_table(page):

    url = "https://rbt.mci.ir/AJAX/latestTones.jsp?pgs=%d" % page
    headers = { 'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8/json',
                'Accept-Encoding':'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Host': 'rbt.mci.ir',
                'Referer':'https://rbt.mci.ir/userindex.jsp',
                #'Cookie':'JSESSIONID=GfxUDmc4AT5FTcCARmB+uHDV.undefined; cookiesession1=9PKTK1LB6USNJIQ4SJU34S63LEUTMF8H; _ga=GA1.2.76051626.1468215694; _gat=1',
                'Content-Length':'0'
            }

    response = requests.post(url,headers=headers)
    return response
