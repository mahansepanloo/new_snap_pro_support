from django.db import models
from django.contrib.auth.models import User


class Subscription(models.Model):
    tital = models.CharField(max_length=500)
    price = models.BigIntegerField()
    interval = models.IntegerField()

    def __str__(self):
        return self.tital


class ProUser(models.Model):
    is_pro = models.BooleanField(default=False)
    user_name = models.CharField(max_length=100)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Pro User: ({self.user_name})"

class ProRestaurant(models.Model):
    name = models.CharField(max_length=100)
    is_pro = models.BooleanField(default=False)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Pro Restaurant: {self.name}"


class Suporter(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_suportet = models.BooleanField(default=False)