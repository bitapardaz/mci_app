from models import MTN_Album, MTN_Song
from mtn_userprofile.models import MTN_UserProfile
from django.contrib.auth.models import User

def move_songs(start,target,number_of_songs):

    sAlbum = MTN_Album.objects.get(id=start)
    tAlbum = MTN_Album.objects.get(id=target)

    songs = MTN_Song.objects.filter(album = sAlbum)[0:number_of_songs]

    for song in songs:

        song.album = tAlbum
        song.save()




def create_bulk_user_from_user_profiles():

    all_profiles = MTN_UserProfile.objects.all()

    for profile in all_profiles:

        username = profile.mobile_number
        new_user = User.objects.create_user(username)

        profile.user = new_user
        profile.save()
