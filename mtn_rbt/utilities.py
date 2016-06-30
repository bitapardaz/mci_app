from models import MTN_Album, MTN_Song

def move_songs(start,target,number_of_songs):

    sAlbum = MTN_Album.objects.get(id=start)
    tAlbum = MTN_Album.objects.get(id=target)

    songs = MTN_Song.objects.filter(album = sAlbum)[0:number_of_songs]

    for song in songs:

        song.album = tAlbum
        song.save()
