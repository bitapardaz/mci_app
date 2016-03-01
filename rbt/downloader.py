from bs4 import BeautifulSoup
import urllib2
from models import Song,Category,Producer


def derive_song_information(html_page):

    soup = BeautifulSoup(html_page,'html.parser')
    table_tag = soup.table

    code = table_tag.find_all('td')[1].string.strip()
    name = table_tag.find_all('td')[3].string.strip()
    producer_farsi = table_tag.find_all('td')[5].string.strip()
    category_farsi = table_tag.find_all('td')[17].string.strip()

    return (code,name,producer_farsi,category_farsi)

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

def add_song_to_db(code,name,producer_farsi,category_farsi):
    # get or create producer
    producer,created = Producer.objects.get_or_create(name=producer_farsi)

    # get or create cateogory
    category,created = Category.objects.get_or_create(name=category_farsi)

    # audio download link
    audio_link = "http://rbt.mci.ir/wave/%s.wav" % code

    # save the song
    song = Song(activation_code=code,
                download_link=audio_link,
                song_name=name,
                producer=producer,
                category=category)
    song.save()


#################################################
### running the downloader
#################################################

for id in range(82050,82113):

    print("%s\n" % id)

    html_page = download_song_html(id)
    if is_song_valid(html_page):

        # get the information from mci site
        (code,name,producer_farsi,category_farsi) = derive_song_information(html_page)

        # check if the song already exists in the database
        try:
            song = Song.objects.get(activation_code=int(code))
            # the song already exists in the database.
            # Do nothing.
        except Song.DoesNotExist:
            add_song_to_db(code,name,producer_farsi,category_farsi)
            print( "song %s added to db." % code )
