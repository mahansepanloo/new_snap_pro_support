from django.contrib import admin
from .models import *
@admin.register(Question)
class ModelNameAdmin(admin.ModelAdmin):
    pass
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
