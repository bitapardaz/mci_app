from rest_framework import serializers
from models import Song,Category,Album,CatAdvert

class SongSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField(read_only=True)
    producer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Song
        fields = ('song_name','activation_code','download_link','rate',
                    'activated','producer','image','category')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album


class CatAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model=CatAdvert
