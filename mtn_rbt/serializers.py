from rest_framework import serializers
from django.core.serializers import serialize as core_serialize
from rest_framework.renderers import JSONRenderer
from models import MTN_Song,MTN_Category,MTN_Album,MTN_CatAdvert,MTN_MainAdvert,MTN_MainPageFeatured


class MTN_SongSerializer(serializers.ModelSerializer):

    #category = serializers.StringRelatedField(read_only=True)
    producer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = MTN_Song
        fields = ('song_name','activation_code','download_link','rate',
                    'activated','producer','image',)


class MTN_CategorySerializer(serializers.ModelSerializer):
    '''
    serializes a category including its children
    '''

    children = serializers.SerializerMethodField('mychildren')

    def mychildren(self,cat):
        children = MTN_Category.objects.filter(parent = cat,confirmed=True)
        if children == []:
            return []
        else:
            return children.values()

    parent = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = MTN_Category
        fields = ('id','farsi_name','display_name','photo','parent','children')



class MTN_AlbumSerializer(serializers.ModelSerializer):

    producer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = MTN_Album


class MTN_CatAdvertSerializer(serializers.ModelSerializer):

    album_detail = serializers.SerializerMethodField('get_album_details')

    def get_album_details(self,ad):

        if ad.album==None:
            return None
        else:
            serializer = MTN_AlbumSerializer(ad.album)
            return serializer.data

    class Meta:
        model=MTN_CatAdvert
        fields = ('id','category','album_detail','miscellaneous','url')


class MTN_MainAdvertSerializer(serializers.ModelSerializer):

    album_detail =  serializers.SerializerMethodField('get_album_details')

    def get_album_details(self,ad):

        if ad.album==None:
            return None
        else:
            serializer = MTN_AlbumSerializer(ad.album)
            return serializer.data

    class Meta:
        model=MTN_MainAdvert
        fields = ('id','miscellaneous','url','album_detail',)
