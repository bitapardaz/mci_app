from models import Album, Song
from userprofile.models import UserProfile
from django.contrib.auth.models import User
from general_user_profile.models import GeneralProfile

def move_songs(start,target,number_of_songs):

    sAlbum = Album.objects.get(id=start)
    tAlbum = Album.objects.get(id=target)

    songs = Song.objects.filter(album = sAlbum)[0:number_of_songs]

    for song in songs:

        song.album = tAlbum
        song.save()


def create_bulk_user_from_user_profiles():

    all_profiles = UserProfile.objects.all()

    for profile in all_profiles:

        username = profile.mobile_number

        new_user = User.objects.create_user(username)
        new_general_profile = GeneralProfile.objects.create(user=new_user,operator='MCI')


        profile.general_profile = new_general_profile
        profile.save()
