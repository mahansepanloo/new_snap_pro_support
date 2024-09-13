from django.urls import path
from .views import *



urlpatterns = [
    path('subscriptions/', SubscriptionListView.as_view()),
    path('subscriptions/request/', SubscriptionRequest.as_view()),
    path('update-pro-user/', UpdateProUser.as_view()),
    path('update-pro-restaurant/', UpdateProRestaurant.as_view()),
    path('SubscriptionRequestRestaurant', SubscriptionRequestRestaurant.as_view()),
    path('SubscriptionListViewRestu', SubscriptionListViewRestu.as_view()),


]