from models import Album, Song, Category


def populate_producer(album):

    if album.producer == None:
        first_song = Song.objects.filter(album=album)[0]
        album.producer = first_song.producer
        album.save()

def populate_producer_pop_songs():

    for album in Album.objects.filter(category__english_name='traditional'):
        populate_producer(album)
