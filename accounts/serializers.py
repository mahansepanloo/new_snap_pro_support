from rest_framework import serializers
from .models import ProUser, ProRestaurant

class ProUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProUser
        fields = ['is_pro', 'start', 'end', 'subscription_type']

class ProRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProRestaurant
        fields = '__all__'
