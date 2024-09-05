from rest_framework import serializers
from .models import ProUser, ProRestaurant

class ProUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProUser
        fields = ['user', 'is_pro', 'start']

class ProRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProRestaurant
        fields = ['user', 'is_pro', 'start']
