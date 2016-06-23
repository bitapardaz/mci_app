from bs4 import BeautifulSoup
import urllib2
import urllib
import json
from urllib2 import HTTPError
from bs4 import BeautifulSoup
from mtn_rbt.models import MTN_Song,MTN_Album, MTN_MusicStudio, MTN_Category, MTN_Producer
from rbt.models import Producer
import os


def run_downloader():

    for tone_id in range(1900,2000):

        print("\n\n%s- checking if the song already exists" % tone_id)

        try:
            # check if the song already exists in the database
            song = MTN_Song.objects.get(tone_id=tone_id)

            # the song already exists in the database.
            print("%s- already exists" % tone_id)
            # Do nothing.

        except MTN_Song.DoesNotExist:

            print("%s- tone_id is new to database. Checking the ID... " % tone_id)

            (is_code_valid,tone_id_2, name, price, singer_name, tone_valid_day,audio_file_path, activation_code, album, category,music_studio) = get_one_song_information(tone_id)

            if is_code_valid:
                print("%s- Adding tone_id to the database... " % tone_id)
                add_song_to_db(tone_id,name,price,singer_name,tone_valid_day,audio_file_path,activation_code,album,category,music_studio)
                print( "(%s,%s)- inserted" % (tone_id,activation_code))

            else:
                print("%s- invalid code" % tone_id)



def add_song_to_db(tone_id,song_name,price,singer_name,tone_valid_day,audio_file_path,activation_code,f_album,f_category,f_music_studio):
    '''
    categories are dynamically created (if it does not previously exist)
    and is associated with the album.
    '''

    # get or create producer
    try:
        producer,created = MTN_Producer.objects.get_or_create(name=singer_name)
    except MTN_Producer.MultipleObjectsReturned:
        producer = MTN_Producer.objects.filter(name=singer_name)[0]


    # get or create music_studio
    try:
        music_studio,created = MTN_MusicStudio.objects.get_or_create(name=f_music_studio)
    except MTN_MusicStudio.MultipleObjectsReturned:
        prmusic_studio = MTN_MusicStudio.objects.filter(name=f_music_studio)[0]


    # get or create cateogory
    category,created = MTN_Category.objects.get_or_create(farsi_name=f_category)

    # get or create the album
    album,created = MTN_Album.objects.get_or_create(farsi_name=f_album,category=category)

    # send song file to the storage server for the purpose of uploading

    # calculate the link to the audio file on the ftp server for the purpose of downloading
    audio_link_ftp_server = generate_ftp_server_audio_path(tone_id)

    # save the song
    mtn_song = MTN_Song(tone_id = tone_id,
                activation_code=activation_code,
                download_link=audio_link_ftp_server,
                song_name=song_name,
                producer=producer,
                album = album,
                confirmed = False,
                music_studio = music_studio,
                )
    mtn_song.save()

    # delete the file from the main server
    if os.path.exists(audio_file_path):
        os.remove(audio_file_path)


def get_one_song_information(tone_id):

    is_code_valid = False

    name = ""
    price = ""
    singer_name = ""
    tone_valid_day = ""
    audio_file_path = ""
    activation_code = ""
    album = ""
    category = ""
    music_studio = ""

    f_tone_id = str(tone_id)
    data = urllib.urlencode({'toneId': f_tone_id })
    url = "http://rbt.irancell.ir/user/qryListenUrlById.screen"
    r = urllib2.Request(url=url,data=data)
    response = urllib2.urlopen(r)
    j_response = json.loads(response.read().strip())

    print "%d- received initial date" % tone_id

    '''
    check if the json is empty.
    '''
    tone_info = j_response['toneInfo']
    if tone_info != None:
        '''
        the json has some information in it, but now we should check
        if the information is valid -- the audio link actually works
        '''

        print "%d- JSON has information in it, checking audio file...." % tone_id


        audio_link = j_response["toneInfo"]["tonePreListenAddress"]
        audio_file = urllib.URLopener()
        audio_file_path = generate_relative_audio_file_path(tone_id)
        try:



            audio_file.retrieve(audio_link,audio_file_path)
            # note: this will save the file on the disk.
            # make sure that you remove the file after it is
            # uploaded on the ftp server.
            is_code_valid = True

            print "%d- Audio file exists... now saving %s" % (tone_id,audio_file_path)

            # extract informatin from json

            f_tone_id = j_response["toneInfo"]["toneID"]
            name = j_response["toneInfo"]["toneName"]
            price = j_response["toneInfo"]["price"]
            singer_name = j_response["toneInfo"]["singerName"]
            tone_valid_day = j_response["toneInfo"]["toneValidDay"]
            audio_link = j_response["toneInfo"]["tonePreListenAddress"]
            activation_code = j_response["toneInfo"]["toneCode"]

            '''
            extract album and category by sending another request
            '''
            (music_studio,category,album) = get_additional_info(f_tone_id)

            print "%d- additional info (album+category+music studio) received" % tone_id
            print "%d- returning all song information to the runner" % tone_id

            return (is_code_valid,f_tone_id, name, price, singer_name, tone_valid_day,
                    audio_file_path, activation_code, album, category,music_studio)


        except (HTTPError, IOError) as e:
            '''
            the code is valid but the audio file does not exist
            return empty result
            '''
            print "Audio file deos not exists ... "
            return (is_code_valid,tone_id, name, price, singer_name, tone_valid_day,
                    audio_file_path, activation_code, album, category,music_studio)

    else:
        '''
        the json is empty. Info:null. The code is not valid
        '''
        print "JSON is empty..."
        return (is_code_valid,tone_id, name, price, singer_name, tone_valid_day,
                audio_file_path, activation_code, album, category,music_studio)




def get_additional_info(f_tone_id):
    '''
    return the album and category of the tone_id
    '''
    url = "http://rbt.irancell.ir/user/showDetailPop.do?toneID=%s&toneCode=0&fortuneFlag=1&isDownload=0&resServType=1&downdate=undefined&serviceID=undefined&keepThis=true&" % f_tone_id
    r = urllib2.Request(url)
    downloaded = urllib2.urlopen(r)
    html_page = downloaded.read()

    soup = BeautifulSoup(html_page,'html.parser')
    table_tag = soup.table
    music_studio = table_tag.find_all('td')[11].string.strip()
    category = table_tag.find_all('td')[13].string.strip()
    album = table_tag.find_all('td')[15].string.strip()

    return (music_studio,category,album)



def generate_relative_audio_file_path(tone_id):
    '''
    returns the name to be used when temporarily saving
    a song to our database. (before sendnig the song to ftp server)
    '''
    return "song_storage/tone_%d" % tone_id


def generate_ftp_server_audio_path(tone_id):
    return "http://pishahangstorage.com/songs/tone_%s.wav" % str(tone_id)
