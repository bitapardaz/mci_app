from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
from models import Song,Category
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import SongSerializer,CategorySerializer
from userprofile.serializers import UserProfileSerializer
from userprofile.models import UserProfile



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


@api_view(['GET'])
def list_all_cats(request,format=None):
    """
    returns the categories and their information
    """
    category_list = Category.objects.all()
    serializer = CategorySerializer(category_list,many=True)
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
        song_list = Song.objects.filter(category__name = cat_name)[start_index:end_index]
        serializer = SongSerializer(song_list,many=True)
        return Response(serializer.data)
