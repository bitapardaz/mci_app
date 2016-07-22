from rest_framework import serializers

from models import TopAdvert,Album,MiddleAdvert

class TopAdvertSerializer(serializers.ModelSerializer):

    album_detail = serializers.SerializerMethodField('get_album_details')

    def get_album_details(self,ad):

        if ad.album==None:
            return None
        else:
            serializer = AlbumSerializer(ad.album)
            return serializer.data

    class Meta:
        model = TopAdvert
        fields = ('id','album','miscellaneous','url','ranking','album_detail')



class AlbumSerializer(serializers.ModelSerializer):

    singer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Album


class MiddleAdvertSerializer(serializers.ModelSerializer):

    album_detail = serializers.SerializerMethodField('get_album_details')

    def get_album_details(self,ad):

        if ad.album==None:
            return None
        else:
            serializer = AlbumSerializer(ad.album)
            return serializer.data

    class Meta:
        model = MiddleAdvert
        fields = ('id','album','miscellaneous','url','ranking','album_detail')
