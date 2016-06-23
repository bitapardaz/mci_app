from rest_framework import serializers
from .models import MTN_UserProfile


class MTN_UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = MTN_UserProfile
