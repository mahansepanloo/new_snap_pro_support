from django.contrib import admin

from .models import *
@admin.register(ProUser)
class ModelNameAdmin(admin.ModelAdmin):
    pass
@admin.register(ProRestaurant)
class ModelNameAdmin(admin.ModelAdmin):
    pass