from django.urls import path
from .views import CreateQ, CreateAnser

urlpatterns = [
    path('questions', CreateQ.as_view(), name='create-question'),
    path('answers', CreateAnser.as_view(), name='create-answer'),
]
