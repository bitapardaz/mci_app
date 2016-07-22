from models import MTN_Album, MTN_Song
from mtn_userprofile.models import MTN_UserProfile
from django.contrib.auth.models import User
from general_user_profile.models import GeneralProfile


def move_songs(start,target,number_of_songs):

    sAlbum = MTN_Album.objects.get(id=start)
    tAlbum = MTN_Album.objects.get(id=target)

    songs = MTN_Song.objects.filter(album = sAlbum)[0:number_of_songs]

    for song in songs:

        song.album = tAlbum
        song.save()




def create_bulk_user_from_user_profiles():

    all_profiles = MTN_UserProfile.objects.all()

    index = 0
    total = len(all_profiles)

    for profile in all_profiles:

        index = index +1

        print "user %d out of %d" % (index,total)

        username = profile.mobile_number

        try:

            user = User.objects.get(username=username)

        except User.DoesNotExist:
            #the user does not exist. we should add it

            new_user = User.objects.create_user(username)
            new_general_profile = GeneralProfile.objects.create(user=new_user,operator='MTN')
            profile.general_profile = new_general_profile

            profile.save()
