from django.contrib import admin
from .models import *


@admin.register(SubscriptionRestaurant)
class SubscriptionRestaurantAdmin(admin.ModelAdmin):
    pass