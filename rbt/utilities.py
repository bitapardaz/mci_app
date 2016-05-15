from models import Album, Song

def move_songs(start,target,number_of_songs):

    sAlbum = Album.objects.get(id=start)
    tAlbum = Album.objects.get(id=target)

    songs = Song.objects.filter(album = sAlbum)[0:number_of_songs]

    for song in songs:

        song.album = tAlbum
        song.save()

def move_allbums(sCat,tcat):

    
