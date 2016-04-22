from rest_framework import serializers
from django.core.serializers import serialize as core_serialize
from rest_framework.renderers import JSONRenderer
from models import Song,Category,Album,CatAdvert,MainAdvert

class SongSerializer(serializers.ModelSerializer):

    #category = serializers.StringRelatedField(read_only=True)
    producer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Song
        fields = ('song_name','activation_code','download_link','rate',
                    'activated','producer','image',)


class CategorySerializer(serializers.ModelSerializer):
    '''
    serializes a category including its children
    '''

    children = serializers.SerializerMethodField('mychildren')

    def mychildren(self,cat):
        children = Category.objects.filter(parent = cat)
        if children == []:
            return []
        else:
            return children.values()

    parent = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Category
        fields = ('farsi_name','display_name','photo','parent','children')



class AlbumSerializer(serializers.ModelSerializer):

    producer = serializers.StringRelatedField(read_only=True)


    class Meta:
        model = Album


class CatAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model=CatAdvert


class MainAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model=MainAdvert
