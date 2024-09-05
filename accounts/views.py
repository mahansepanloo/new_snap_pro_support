from rest_framework import generics
from .models import ProUser,ProRestaurant
from .serializers import ProUserSerializer,ProRestaurantSerializer

class ProUserListCreateView(generics.ListCreateAPIView):
    queryset = ProUser.objects.all()
    serializer_class = ProUserSerializer

class ProUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProUser.objects.all()
    serializer_class = ProUserSerializer

class ProRestaurantListCreateView(generics.ListCreateAPIView):
    queryset = ProRestaurant.objects.all()
    serializer_class = ProRestaurantSerializer

class ProRestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProRestaurant.objects.all()
    serializer_class = ProRestaurantSerializer