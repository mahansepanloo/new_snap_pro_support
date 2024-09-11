from django.urls import path
from .views import SubscriptionListView, SubscriptionRquest,CreateProUser

urlpatterns = [
    path('subscriptions/', SubscriptionListView.as_view()),
    path('subscriptions/request/', SubscriptionRquest.as_view()),
    path('create-pro-user/', CreateProUser.as_view()),
]