from django.urls import path
from .views import  ProUserDetailView, ShowAllUsers, ProRestaurantDetailView,ShowAllRestorant

urlpatterns = [
    path('pro_users/', ShowAllUsers.as_view(), name='pro_user_list_create'),
    path('pro_users/<int:pk>/', ProUserDetailView.as_view(), name='pro_user_detail'),
    path('pro_restaurants/', ShowAllRestorant.as_view(), name='pro_restaurant_list_create'),
    path('pro_restaurants/<int:pk>/', ProRestaurantDetailView.as_view(), name='pro_restaurant_detail'),
]