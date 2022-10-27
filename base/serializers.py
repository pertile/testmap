from base.models import UserProfile
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class ProfileSerializer(GeoFeatureModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        geo_field = 'location'
        fields = ['user', 'home_address', 'phone_number', 'location']
    
