from rest_framework import serializers
from models import UserProfile,ActivationRequest


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile

class ActivationRequestSerializer(serializers.ModelSerializer):

    user_profile = serializers.SlugRelatedField(read_only=True,
                                                many=True,
                                                slug_field='mobile_number')

    class Meta:
        model = ActivationRequest
        fields = ('user_profile','song','WhereAmI','activated')
