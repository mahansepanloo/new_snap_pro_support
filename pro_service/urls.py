from django.urls import path
from .views import (
    SubscriptionListView,
    SubscriptionRequest,
    CreateProUser,
    CreateProRestaurant,
    SubscriptionRequestRestaurant,
    SubscriptionListViewRestu
)

urlpatterns = [
    path('subscriptions/', SubscriptionListView.as_view()),
    path('subscriptions/request/', SubscriptionRequest.as_view()),
    path('create-pro-user/', CreateProUser.as_view()),
    path('create-pro-restaurant/', CreateProRestaurant.as_view()),
    path('subscription-restaurant-request/', SubscriptionRequestRestaurant.as_view()),
    path('subscription-restaurant/', SubscriptionListViewRestu.as_view()),
]