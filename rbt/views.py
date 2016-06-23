from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
from models import Song,Category,Album,CatAdvert,MainAdvert,MainPageFeatured, Category_Featured, Search_Activity
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import SongSerializer,CategorySerializer,AlbumSerializer, CatAdvertSerializer,MainAdvertSerializer
from userprofile.serializers import UserProfileSerializer
from userprofile.models import UserProfile
from forms import AlbumSelectForm
from django.core import serializers
import itertools

@api_view(['GET'])
def homepage(request,format=None):

    dict = {}
    ads = MainAdvert.objects.all()
    serializer = MainAdvertSerializer(ads,many=True)
    dict['ads'] = serializer.data

    featured_albums = []
    recommendations = MainPageFeatured.objects.all().order_by('-date_published')
    for recom in recommendations:
        featured_albums.append(recom.album)
    serializer = AlbumSerializer(featured_albums,many=True)
    dict['featured_albums'] = serializer.data

    new_items = Album.objects.filter(confirmed=True).order_by('-date_published')[0:20]
    serializer = AlbumSerializer(new_items,many=True)
    dict['new_albums'] = serializer.data

    popular_albums = Album.objects.filter(confirmed=True).order_by('-rate')[0:20]
    serializer = AlbumSerializer(popular_albums,many=True)
    dict['popular_albums'] = serializer.data

    cat_list = Category.objects.filter(confirmed=True,parent=None)
    serializer = CategorySerializer(cat_list,many=True)
    dict['categories'] = serializer.data

    response =  Response(dict)
    return response

@api_view(['GET'])
def cat_homepage(request,cat_id):

    dict={}

    category = Category.objects.get(id=cat_id)

    # children
    # depends on wehether the category has children or not
    child_list = Category.objects.filter(confirmed=True,parent=category)
    serializer = CategorySerializer(child_list,many=True)
    dict['categories'] = serializer.data

    # get cat ads
    ads = CatAdvert.objects.filter(category=category)
    serializer = CatAdvertSerializer(ads,many=True)
    dict['ads'] = serializer.data

    # get  our recommendations (featured) for the category
    featured_albums = []
    recommendations = Category_Featured.objects.filter(category = category).order_by('-date_published')
    for recom in recommendations:
        featured_albums.append(recom.album)
    serializer = AlbumSerializer(featured_albums,many=True)
    dict['featured_albums'] = serializer.data

    # new albums in this category
    # depends on whether the category has children or not.
    album_list = get_category_new_albums(category,child_list)
    serializer = AlbumSerializer(album_list,many=True)
    dict['new_albums'] = serializer.data

    # popular albums in this cateogory
    # depends on whether the category has children or not.
    album_list = get_category_popular_albums(category,child_list)
    serializer = AlbumSerializer(album_list,many=True)
    dict['popular_albums'] = serializer.data

    response = Response(dict)
    return response



def get_category_new_albums(category,child_list):
    '''
    returns the albums associated with this category. If the category
    has children, then the latest albums in each child are also included.
    '''
    if len(child_list) == 0:
        albums = Album.objects.filter(category = category,confirmed=True).order_by('-date_published')[0:20]

    else: # the category has some children.
        child_albums = []
        for child in child_list:
            album_list = Album.objects.filter(category=child,confirmed=True).order_by('-date_published')[0:10]
            child_albums.append(album_list)

        albums = sorted( itertools.chain.from_iterable(child_albums) , key=lambda instance: instance.date_published, reverse=True )

    return albums


def get_category_popular_albums(category,child_list):
    '''
    returns the popular albums associated with this category. If the category
    has children, then the popular albums in each child are also included.
    '''
    if len(child_list) == 0:
        albums = Album.objects.filter(category = category,confirmed=True).order_by('-rate')[0:20]
    else: # the category has some children.

        child_albums = []
        for child in child_list:
            album_list = Album.objects.filter(category=child,confirmed=True).order_by('-rate')[0:10]
            child_albums.append(album_list)

        albums = itertools.chain.from_iterable(child_albums)

    return albums


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

    '''
    returns the albums in the current category and its
    children ordered based on the date-published.
    '''

    page_index = int(page)
    no_of_items = 20
    start_index = page_index * no_of_items
    end_index = (page_index+1) * no_of_items

    #print "start_index:%d" % start_index
    #print "end_index:%d" % end_index

    # children
    category = Category.objects.get(id=cat_id)
    child_list = Category.objects.filter(confirmed=True,parent=category)

    if len(child_list) == 0:
        albums = Album.objects.filter(category=category,confirmed=True).order_by('-date_published')[start_index:end_index]
        serializer = AlbumSerializer(albums,many=True)
        return Response(serializer.data)

    else: # the category has some children. The first no_of_items of each category is taken
        child_albums = []
        for child in child_list:
            album_list = Album.objects.filter(category=child,confirmed=True).order_by('-date_published')[start_index:end_index]
            child_albums.append(album_list)


        albums = itertools.chain.from_iterable(child_albums)
#        final_albums =  [album for album in albums]
#        length = len(final_albums)
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
def latest_albums(request,page,format=None):
    """
    returns the latest albums across all categories and the
    results is displayed in the first page.
    """
    step = 30

    page_index = int(page)
    start_index = page_index * step
    end_index = (page_index+1) * step

    album_list = Album.objects.filter(confirmed=True).order_by('-date_published')[start_index:end_index]
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

            token = serializer.validated_data['token']
            if token != "":
                obj.token = token
                obj.save()

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

    # add albums in the children.
    children = Category.objects.filter(parent=category)
    for child in children:
        child_album = Album.objects.filter(category=child,confirmed=True).order_by('-date_published')
        albums = albums | child_album

    serializer = AlbumSerializer(albums,many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def search(request,format=None):
    """
    search functionality.
    Album name.
    """

    if request.method == 'POST':

        term = request.data.get('term')

        # inset search term in Search_Activity Table
        search = Search_Activity.objects.create(search_term=term)

        # gather search result

        dict = {}

        # search based on album title
        albums = Album.objects.filter(confirmed=True, farsi_name__contains = term).order_by('-date_published')[0:20]
        serializer = AlbumSerializer(albums,many=True)
        dict['albums'] = serializer.data


        # search based on song_name and then return the albums
        song_albums = song_album_search_utility(term,page=0)
        serializer = AlbumSerializer(song_albums,many=True)
        dict['song_albums'] = serializer.data

        # search based on producer name of the songs
        producer_albums = producer_album_search_utility(term,page=0)
        serializer = AlbumSerializer(producer_albums,many=True)
        dict['producer_albums'] = serializer.data

        response = Response(dict)
        return response

    else:
        return Response("POST your search term.")







@api_view(['GET','POST'])
def search_album_more(request,page,format=None):
    """
    search functionality.
    Album name.
    """

    if request.method=="POST":

        term = request.data.get('term')
        page =  int(page)

        step = 20
        start_index = page * step
        end_index = (page+1) * step

        dict = {}

        albums = Album.objects.filter(confirmed=True, farsi_name__contains = term).order_by('-date_published')[start_index:end_index]
        serializer = AlbumSerializer(albums,many=True)
        dict['albums'] = serializer.data

        response = Response(dict)
        return response

    else:
            return Response("POST your search term.")



@api_view(['GET','POST'])
def search_song_albums_more(request,page,format=None):
    """
    search functionality.
    Song name
    """

    page =  int(page)

    if request.method == "POST":

        dict = {}
        term = request.data.get('term')

        song_albums = song_album_search_utility(term,page)
        serializer = AlbumSerializer(song_albums,many=True)
        dict['song_albums'] = serializer.data

        response = Response(dict)
        return response

    else:
        return Response("POST your search term.")



@api_view(['GET','POST'])
def search_producer_albums_more(request,page,format=None):
    """
    search functionality.
    producer name
    """

    page =  int(page)

    if request.method == "POST":

        dict = {}
        term = request.data.get('term')

        producer_albums = producer_album_search_utility(term,page)
        serializer = AlbumSerializer(producer_albums,many=True)
        dict['producer_albums'] = serializer.data

        response = Response(dict)
        return response

    else:

        return Response("POST your search term.")



def song_album_search_utility(term,page):

    # number of songs that are taken into account.
    # note: a song might be in an album with confirmed = False
    # thus, we take a lot of songs in each uptake.
    step = 200

    start_index = page * step
    end_index = (page+1) * step

    song_albums = set()
    songs = Song.objects.filter(album__confirmed=True ,song_name__contains=term)[start_index:end_index].select_related('album')
    for song in songs:
        song_albums.add(song.album)

    return song_albums

def producer_album_search_utility(term,page):


    # number of songs that are taken into account.
    # note: a song might be in an album with confirmed = False
    # thus, we take a lot of songs in each uptake.
    step = 200

    start_index = page * step
    end_index = (page+1) * step


    producer_albums = set()
    songs = Song.objects.filter(album__confirmed=True,producer__name__contains=term)[start_index:end_index].select_related('album')
    for song in songs:
        producer_albums.add(song.album)

    return producer_albums
