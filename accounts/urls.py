from django.urls import path
from .views import  ProUserDetailView, ProRestaurantListCreateView, ProRestaurantDetailView

urlpatterns = [
    # path('pro_users/', ProUserListCreateView.as_view(), name='pro_user_list_create'),
    path('pro_users/<int:pk>/', ProUserDetailView.as_view(), name='pro_user_detail'),
    path('pro_restaurants/', ProRestaurantListCreateView.as_view(), name='pro_restaurant_list_create'),
    path('pro_restaurants/<int:pk>/', ProRestaurantDetailView.as_view(), name='pro_restaurant_detail'),
]