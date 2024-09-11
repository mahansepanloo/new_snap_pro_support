from rest_framework import serializers
from .models import ProUser, ProRestaurant

class ProUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProUser
        fields = '__all__'

class ProRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProRestaurant
        fields = '__all__'
