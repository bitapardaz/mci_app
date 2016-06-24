from django.shortcuts import render

from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
from mtn_rbt.models import MTN_Song,MTN_Category,MTN_Album,MTN_CatAdvert,MTN_MainAdvert,MTN_MainPageFeatured, MTN_Category_Featured, MTN_Search_Activity
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import MTN_SongSerializer,MTN_CategorySerializer,MTN_AlbumSerializer, MTN_CatAdvertSerializer,MTN_MainAdvertSerializer
from mtn_userprofile.serializers import MTN_UserProfileSerializer
from mtn_userprofile.models import MTN_UserProfile
#from forms import AlbumSelectForm
from django.core import serializers
import itertools


# Create your views here.

@api_view(['POST'])
def register(request,format=None):
    """
    creates a new mobile phone number
    """
    if request.method == 'POST':

        serializer = MTN_UserProfileSerializer(data=request.data)
        if serializer.is_valid():

            # extract mobile number
            mobile_number = serializer.validated_data['mobile_number']
            obj, created = MTN_UserProfile.objects.get_or_create(mobile_number=mobile_number)

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


@api_view(['GET'])
def homepage(request,format=None):

    dict = {}
    ads = MTN_MainAdvert.objects.all()
    serializer = MTN_MainAdvertSerializer(ads,many=True)
    dict['ads'] = serializer.data

    featured_albums = []
    recommendations = MTN_MainPageFeatured.objects.all().order_by('-date_published')
    for recom in recommendations:
        featured_albums.append(recom.album)
    serializer = MTN_AlbumSerializer(featured_albums,many=True)
    dict['featured_albums'] = serializer.data

    new_items = MTN_Album.objects.filter(confirmed=True).order_by('-date_published')[0:20]
    serializer = MTN_AlbumSerializer(new_items,many=True)
    dict['new_albums'] = serializer.data

    popular_albums = MTN_Album.objects.filter(confirmed=True).order_by('-rate')[0:20]
    serializer = MTN_AlbumSerializer(popular_albums,many=True)
    dict['popular_albums'] = serializer.data


    cat_list = MTN_Category.objects.filter(confirmed=True,parent=None)
    serializer = MTN_CategorySerializer(cat_list,many=True)
    dict['categories'] = serializer.data

    response =  Response(dict)
    return response


@api_view(['GET'])
def cat_homepage(request,cat_id):

    dict={}

    category = MTN_Category.objects.get(id=cat_id)

    # children
    # depends on wehether the category has children or not
    child_list = MTN_Category.objects.filter(confirmed=True,parent=category)
    serializer = MTN_CategorySerializer(child_list,many=True)
    dict['categories'] = serializer.data

    # get cat ads
    ads = MTN_CatAdvert.objects.filter(category=category)
    serializer = MTN_CatAdvertSerializer(ads,many=True)
    dict['ads'] = serializer.data

    # get our recommendations (featured) for the category
    featured_albums = []
    recommendations = MTN_Category_Featured.objects.filter(category = category).order_by('-date_published')
    for recom in recommendations:
        featured_albums.append(recom.album)
    serializer = MTN_AlbumSerializer(featured_albums,many=True)
    dict['featured_albums'] = serializer.data

    # new albums in this category
    # depends on whether the category has children or not.
    album_list = get_category_new_albums(category,child_list)
    serializer = MTN_AlbumSerializer(album_list,many=True)
    dict['new_albums'] = serializer.data

    # popular albums in this cateogory
    # depends on whether the category has children or not.
    album_list = get_category_popular_albums(category,child_list)
    serializer = MTN_AlbumSerializer(album_list,many=True)
    dict['popular_albums'] = serializer.data

    response = Response(dict)
    return response


def get_category_new_albums(category,child_list):
    '''
    returns the latest albums associated with this category. If the category
    has children, then the latest albums in each child are also included.
    '''
    if len(child_list) == 0:
        albums = MTN_Album.objects.filter(category = category,confirmed=True).order_by('-date_published')[0:20]

    else: # the category has some children.
        child_albums = []
        for child in child_list:
            album_list = MTN_Album.objects.filter(category=child,confirmed=True).order_by('-date_published')[0:20]
            child_albums.append(album_list)

        albums = sorted( itertools.chain.from_iterable(child_albums) , key=lambda instance: instance.date_published, reverse=True )

    return albums


def get_category_popular_albums(category,child_list):
    '''
    returns the popular albums associated with this category. If the category
    has children, then the popular albums in each child are also included.
    '''
    if len(child_list) == 0:
        albums = MTN_Album.objects.filter(category = category,confirmed=True).order_by('-rate')[0:20]
    else: # the category has some children.

        child_albums = []
        for child in child_list:
            album_list = MTN_Album.objects.filter(category=child,confirmed=True).order_by('-rate')[0:10]
            child_albums.append(album_list)

        albums = sorted( itertools.chain.from_iterable(child_albums) , key=lambda instance: instance.rate, reverse=True )

    return albums
