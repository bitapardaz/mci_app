from django.shortcuts import render

from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
from mtn_rbt.models import MTN_Song,MTN_Category,MTN_Album,MTN_CatAdvert,MTN_MainAdvert,MTN_MainPageFeatured, MTN_Category_Featured, MTN_Search_Activity
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from serializers import MTN_SongSerializer,MTN_CategorySerializer,MTN_AlbumSerializer, MTN_CatAdvertSerializer,MTN_MainAdvertSerializer
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
