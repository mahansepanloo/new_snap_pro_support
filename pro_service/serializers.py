from rest_framework import serializers
from .models import  Subscription, SubscriptionRestaurant

class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = "__all__"

class ProRestaurantsubSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionRestaurant
        fields = "__all__"