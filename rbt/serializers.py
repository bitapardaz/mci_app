from rest_framework import serializers
from models import Song,Category

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('song_name','activation_code','download_link','rate',
                    'activated','producer','image','category')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
