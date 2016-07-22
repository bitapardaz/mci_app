from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

from models import TopAdvert, MiddleAdvert

from serializers import TopAdvertSerializer,AlbumSerializer

# Create your views here.
@api_view(['GET'])
def homepage(request,format=None):

    dict={}

    # get the top ads
    top_ads = TopAdvert.objects.all().order_by('ranking')
    serializer = TopAdvertSerializer(top_ads,many=True)
    dict['top_ads'] = serializer.data

    # get the middle ads
    middle_ads = MiddleAdvert.objects.all().order_by('ranking')
    serializer = TopAdvertSerializer(middle_ads,many=True)
    dict['middle_ads'] = serializer.data

    



    return Response(dict)
