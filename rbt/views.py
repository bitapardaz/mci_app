from django.shortcuts import render
from django.http import HttpResponse
from models import Song
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import SongSerializer


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
