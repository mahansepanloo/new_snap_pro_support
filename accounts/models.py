from django.db import models
from django.contrib.auth.models import User
from pro_service.models import Subscription, SubscriptionRestaurant


class ProUser(models.Model):
    is_pro = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(null=True, blank=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, blank=True, null=True)
    subscription_type = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f"Pro User: ({self.phone_number})"

class ProRestaurant(models.Model):
    restaurant_name = models.CharField(max_length=100)
    is_pro = models.BooleanField(default=False)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(null=True, blank=True)
    subscription = models.ForeignKey(SubscriptionRestaurant, on_delete=models.CASCADE, blank=True, null=True)
    subscription_type = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Pro Restaurant: {self.restaurant_name}"


class Suporter(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_suportet = models.BooleanField(default=False)