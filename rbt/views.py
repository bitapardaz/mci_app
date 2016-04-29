from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
from models import Song,Category,Album,CatAdvert,MainAdvert,MainPageFeatured
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import SongSerializer,CategorySerializer,AlbumSerializer, CatAdvertSerializer,MainAdvertSerializer
from userprofile.serializers import UserProfileSerializer
from userprofile.models import UserProfile
from forms import AlbumSelectForm
from django.core import serializers

@api_view(['GET'])
def homepage(request,format=None):

    dict = {}
    ads = MainAdvert.objects.all()
    serializer = MainAdvertSerializer(ads,many=True)
    dict['main_ads'] = serializer.data

    featured_albums = []
    recommendations = MainPageFeatured.objects.all().order_by('date_published')
    for recom in recommendations:
        featured_albums.append(recom.album)
    serializer = AlbumSerializer(featured_albums,many=True)
    dict['our_recommendation'] = serializer.data

    new_items = Album.objects.filter(confirmed=True).order_by('date_published')[0:20]
    serializer = AlbumSerializer(new_items,many=True)
    dict['new_items'] = serializer.data

    popular_albums = Album.objects.filter(confirmed=True).order_by('rate')[0:20]
    serializer = AlbumSerializer(popular_albums,many=True)
    dict['popular_albums'] = serializer.data

    cat_list = Category.objects.filter(confirmed=True,parent=None)
    serializer = CategorySerializer(cat_list,many=True)
    dict['categories'] = serializer.data

    response =  Response(dict)
    return response

@api_view(['GET']):
def cat_homepage(request,cat_id)

    dict={}

    # get cat ads
    

    # get  our recommendations for the category

    # new albums in this category

    # popular albums in this cateogory

    # children

    #
    response = Response(dict)
    return response

def get_category_by_id(cat_list, id):

    for cat in cat_list:
        if cat.id == id :
            return cat


@api_view(['GET'])
def rbt_cats(request,format=None):
    """
    returns categories related to rbt songs that have been verified.
    Only top level catories are returned, i.e. those with parent=none
    """
    cat_list = Category.objects.filter(confirmed=True,parent=None)
    serializer = CategorySerializer(cat_list,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def cat_albums(request,cat_id,page,format=None):

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

    album_list = Album.objects.filter(category__id = cat_id,confirmed=True).order_by('-rate')[start_index:end_index]
    serializer = AlbumSerializer(album_list,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def cat_new_albums(request,cat_id):
    """
    returns the top 20 most popular albums in the given category
    """
    start_index = 0
    end_index = 20
    album_list = Album.objects.filter(category__id = cat_id,confirmed=True).order_by('-date_published')[start_index:end_index]
    serializer = AlbumSerializer(album_list,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def cat_adverts(request,cat_id,format=None):
    """
    returns the adverts related to the given category.
    """
    ads = CatAdvert.objects.filter(category__id=cat_id)
    albums = [ad.album for ad in ads ]
    serializer = AlbumSerializer(albums,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def main_adverts(request):
    """
    returns the adverts that appear on the first page.
    """
    ads = MainAdvert.objects.all()
    serializer = MainAdvertSerializer(ads,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_album_songs(request,album_id):

    songs = Song.objects.filter(album__id=album_id)
    serializer = SongSerializer(songs,many=True)
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


def album_select(request):

    if request.method == 'GET':

        form = AlbumSelectForm()
        context = {}
        context['form'] = form

        return render(request,'rbt/select_album.html',context)

    if request.method == 'POST':
        return HttpResponse("you are posting")


@api_view(['GET'])
def filter_albums_per_cat(request,format=None):

    cat_id = int(request.GET['cat_id'])
    category = Category.objects.get(pk=cat_id)
    albums = Album.objects.filter(category=category,confirmed=True).order_by('-date_published')
    serializer = AlbumSerializer(albums,many=True)
    return Response(serializer.data)
