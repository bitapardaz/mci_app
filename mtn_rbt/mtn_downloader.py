from bs4 import BeautifulSoup
import urllib2
import urllib
import json
from urllib2 import HTTPError
from bs4 import BeautifulSoup
from mtn_rbt.models import MTN_Song,MTN_Album, MTN_MusicStudio, MTN_Category, MTN_Producer
from rbt.models import Producer
import os
import ftplib



def run_downloader(start_page,end_page):

    all_valid_tones = get_all_valid_tone_codes(start_page,end_page)
    db_tones = MTN_Song.objects.values_list('tone_id',flat=True)
    db_tones_int = [int(item) for item in db_tones]

    new_tones = [ tone for tone in all_valid_tones if tone not in db_tones_int]
    excess_tones = [tone for tone in db_tones_int if tone not in all_valid_tones]

    # open the ftp session to pishahangstorage.com
    host = "46.4.87.118"
    username = "songs@pishahangstorage.com"
    password = "pishahang1234"
    ftp_session = ftplib.FTP(host,username,password)
    print "ftp_session established"


    # adding new_tones
    counter = 0
    for tone_id in new_tones:

        counter = counter + 1
        print("\n\n%s- song %d out of %d " % (tone_id,counter,len(all_valid_tones)))

        print("%s- checking if the song already exists" % tone_id)
        try:
            # check if the song already exists in the database
            song = MTN_Song.objects.get(tone_id=tone_id)

            # the song already exists in the database.
            print("%s- already exists" % tone_id)
            # Do nothing.

        except MTN_Song.DoesNotExist:
            print("%s- tone_id is new to database. Checking the ID... " % tone_id)
            (is_code_valid,f_tone_id, name, price, singer_name,tone_valid_day, activation_code, album, category,music_studio,file_name,audio_file_path,audio_file_ftp_server) = get_one_song_information(tone_id)

            if is_code_valid:
                print("%s- Adding tone_id to the database... " % tone_id)
                add_song_to_db(tone_id,name,price,singer_name,tone_valid_day, activation_code,album,category,music_studio,file_name,audio_file_path, audio_file_ftp_server, ftp_session)
                print( "(%s,%s)- inserted" % (tone_id,activation_code))

            else:
                print("%s- invalid code" % tone_id)


    print "quiting ftp_session"
    ftp_session.quit()

    print "Number of Newly added songs: %d" % len(new_tones)
    # removing excess_tones
    for tone_id in excess_tones:
        song = MTN_Song.objects.get(tone_id=str(tone_id))
        #song.delete()
        print "EXCESS SONG: tone_id: %s" % song.tone_id


def add_song_to_db(tone_id,song_name,price,singer_name,tone_valid_day,activation_code,f_album,f_category,f_music_studio,file_name,audio_file_path, audio_file_ftp_server, ftp_session):
    '''
    categories are dynamically created (if it does not previously exist)
    and is associated with the album.
    '''

    print "%d- adding song to db. music_studio: %s" % (tone_id,f_music_studio)

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

    # send song file to the storage server
    #upload_file_to_ftp_server(tone_id,ftp_session,audio_file_path,file_name)

    # save the song
    mtn_song = MTN_Song(tone_id = tone_id,
                activation_code=activation_code,
                download_link=audio_file_ftp_server,
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
    file_name=""
    audio_file_ftp_server=""

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

        file_name = generate_file_name(tone_id,audio_link)
        audio_file_path = generate_relative_audio_file_path(file_name)

        try:

            print "%d- audio link: %s" % (tone_id,audio_link)
            print "%d- audio local path: %s" % (tone_id,audio_file_path)
            audio_file.retrieve(audio_link,audio_file_path)
            # note: this will save the file on the disk.
            # make sure that you remove the file after it is
            # uploaded on the ftp server.
            is_code_valid = True

            print "%d- Audio file exists... now saving %s" % (tone_id,audio_file_path)

            # extract informatin from json

            f_tone_id = j_response["toneInfo"]["toneID"]
            name = j_response["toneInfo"]["toneName"]
            print "%d- song name: %s" % (tone_id,name)
            price = j_response["toneInfo"]["price"]
            singer_name = j_response["toneInfo"]["singerName"]
            tone_valid_day = j_response["toneInfo"]["toneValidDay"]
            activation_code = j_response["toneInfo"]["toneCode"]

            '''
            extract album and category by sending another request
            '''
            (music_studio,category,album) = get_additional_info(f_tone_id)

            print "%d- additional info (album+category+music studio) received" % tone_id
            print "%d- returning all song information to the runner" % tone_id

            audio_file_ftp_server = generate_ftp_server_file_address(file_name)
            print "%d- ftp server address: %s" % (tone_id,audio_file_ftp_server)

            return (is_code_valid,f_tone_id, name, price, singer_name,
                    tone_valid_day, activation_code, album, category,music_studio,
                    file_name,audio_file_path,audio_file_ftp_server)


        except (HTTPError, IOError) as e:
            '''
            the code is valid but the audio file does not exist
            return empty result
            '''
            print "%d- Audio file deos not exists ... " % tone_id
            return (is_code_valid,f_tone_id, name, price, singer_name,
                    tone_valid_day, activation_code, album, category,music_studio,
                    file_name,audio_file_path,audio_file_ftp_server)


    else:
        '''
        the json is empty. Info:null. The code is not valid
        '''
        print "JSON is empty..."
        return (is_code_valid,f_tone_id, name, price, singer_name,
                tone_valid_day, activation_code, album, category,music_studio,
                file_name,audio_file_path,audio_file_ftp_server)




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



def generate_relative_audio_file_path(file_name):
    return "song_storage/%s" % file_name

def generate_file_name(tone_id,audio_link):

    '''
    returns the name to be used when saving
    a song to our database or uploading on the ftp server.
    the file can be .mp3 or .wav
    '''

    if audio_link.endswith('mp3'):
        return "tone_%d.mp3" % tone_id

    elif audio_link.endswith('wav'):
        return "tone_%d.wav" % tone_id



def generate_ftp_server_file_address(file_name):
    return "http://pishahangstorage.com/songs/%s" % file_name


def upload_file_to_ftp_server(tone_id, ftp_session,audio_file_path,file_name):

    print "%s- uploading to the ftp server" % tone_id

    absoulte_path = os.path.abspath(audio_file_path)
    myfile = open(absoulte_path,'rb')

    command = "STOR %s" % file_name

    print "%s- ftp command: %s" % (tone_id,command)

    ftp_session.storbinary(command,myfile)
    myfile.close()

    print "%s- upload done!" % tone_id




def get_all_valid_tone_codes(start_page,end_page):

    tone_ids = []

    for page in range(start_page,end_page):
        new_ids = get_valid_tone_codes(page)
        tone_ids = tone_ids + new_ids

    print "\n\nTotal number of songs = %d" % len(tone_ids)
    return tone_ids


def get_valid_tone_codes(page):

    new_tone_ids=[]

    website_link = "http://rbt.irancell.ir/user/browseordinarybyname.do?orderBy=2&urlFlag=101&uploadType=&resourceServiceType=1&toneNameLetter=&page=%d" % page

    print "\ndownloading the page from rbt.irancell.com. page=%d" % page
    html = urllib2.urlopen(website_link)
    soup = BeautifulSoup(html,'html.parser')

    for span in soup.find_all('span',class_="w75 txtCent"):

        my_link = span.a
        if my_link != None:
            #Let "link" be a <a> tag that satisfies the condition above

            on_click_text = my_link['onclick']
            #print "onclick text = %s" % on_click_text

            splited_str= on_click_text.split(',')
            tone_id_section = splited_str[1]
            tone_id_string = tone_id_section.split('\'')[1]
            tone_id = int(tone_id_string)
            print "identified tone_id:%d" % tone_id

            new_tone_ids = new_tone_ids + [tone_id]

    return  new_tone_ids
