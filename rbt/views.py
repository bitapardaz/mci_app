from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
from models import Song,Category,Album
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import SongSerializer,CategorySerializer,AlbumSerializer
from userprofile.serializers import UserProfileSerializer
from userprofile.models import UserProfile


@api_view(['GET'])
def rbt_cats(request,format=None):
    """
    returns categories related to rbt songs that have been verified.
    """
    cat_list = Category.objects.filter(confirmed=True)
    serializer = CategorySerializer(cat_list,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def cat_albums(request,cat_id,page):

    page_index = int(page)
    no_of_items = 20
    start_index = page_index * no_of_items
    end_index = start_index + (    ((page_index+1) * no_of_items)   )

    category = Category.objects.get(pk=cat_id)
    albums = Album.objects.filter(category=category,confirmed=True).order_by('-date_published')[start_index:end_index]
    serializer = AlbumSerializer(albums,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def cat_popular_albums(request,cat_id):
    """
    returns the top 20 most popular albums in the given category
    """
    start_index = 0
    end_index = 20
    album_list = Album.objects.all().order_by('-rate')[start_index:end_index]
    serializer = AlbumSerializer(album_list,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def cat_new_albums(request,cat_id):
    """
    returns the top 20 most popular albums in the given category
    """
    start_index = 0
    end_index = 20
    album_list = Album.objects.all().order_by('-date_published')[start_index:end_index]
    serializer = AlbumSerializer(album_list,many=True)
    return Response(serializer.data)





@api_view(['GET'])
def latest_songs(request,page,format=None):
    """
    returns the newest songs.
    """
    page_index = int(page)
    start_index = page_index * 10
    end_index = start_index + 9

    song_list = Song.objects.all().order_by('-date_published')[start_index:end_index]
    serializer = SongSerializer(song_list,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def popular_songs(request,page,format=None):
    """
    returns the songs that have the highest rates given the page number.
    """
    page_index = int(page)
    start_index = page_index * 10
    end_index = start_index + 9

    song_list = Song.objects.all().order_by('-rate')[start_index:end_index]
    serializer = SongSerializer(song_list,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def register(request,format=None):
    """
    creates a new mobile phone number
    """
    if request.method == 'POST':

        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            # extract mobile number
            mobile_number = serializer.validated_data['mobile_number']
            obj, created = UserProfile.objects.get_or_create(mobile_number=mobile_number)
            obj.imei = serializer.validated_data['imei']

            result = {}
            if created:
                result['outcome'] = "new_customer"
                return Response(result,status=status.HTTP_201_CREATED)

            else:
                result['outcome'] = "returning_customer"
                return Response(result, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def list(request,format=None):
    """
    List all songs.
    """

    if request.method =='GET':
        song_list = Song.objects.all()
        serializer = SongSerializer(song_list,many=True)
        return Response(serializer.data)


@api_view(['GET','POST'])
def list_cat(request,cat_name,page,format=None):
    """
    List songs within the page slice.
    slice step is 10
    """

    page_index = int(page)
    start_index = page_index * 10
    end_index = start_index + 9

    if request.method =='GET':
        cat = Category.objects.get(english_name=cat_name)
        song_list = Song.objects.filter(category = cat)[start_index:end_index]
        serializer = SongSerializer(song_list,many=True)
        return Response(serializer.data)
