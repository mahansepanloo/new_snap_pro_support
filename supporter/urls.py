from django.urls import path
from .views import CreateQ, CreateAnser,Login,Refresh

urlpatterns = [
    path('login', Login.as_view()),
    path('Refresh', Refresh.as_view()),
    path('questions', CreateQ.as_view(), name='create-question'),
    path('answers', CreateAnser.as_view(), name='create-answer'),
]
