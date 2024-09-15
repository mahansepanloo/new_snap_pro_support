from rest_framework import generics
from .models import ProUser,ProRestaurant
from .serializers import ProUserSerializer, ProRestaurantSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ShowAllUsers(generics.ListAPIView):
    """
       API View to retrieve a list of all ProUser instances.

       Permissions:
           - Admin users only (IsAdminUser)

       Responses:
           - 200: A list of ProUser objects is returned.
           - 403: User is not an admin.
       """
    queryset = ProUser.objects.all()
    serializer_class = ProUserSerializer
    permission_classes = [IsAdminUser]



class ShowAllRestorant(generics.ListAPIView):
    """
       API View to retrieve a list of all ProRestaurant instances.

       Permissions:
           - Admin users only (IsAdminUser)

       Responses:
           - 200: A list of ProRestaurant objects is returned.
           - 403: User is not an admin.
       """
    queryset = ProRestaurant.objects.all()
    serializer_class = ProRestaurantSerializer
    permission_classes = [IsAdminUser]


class ProUserDetailView(generics.RetrieveAPIView):
    """
       API View to retrieve a ProUser instance by its ID.

       Permissions:
           - Authenticated users only (IsAuthenticated)

       Path Parameters:
           - id: The ID of the ProUser to be retrieved.

       Responses:
           - 200: The ProUser object is returned.
           - 404: ProUser instance does not exist.
           - 403: User is not authenticated.
       """
    queryset = ProUser.objects.all()
    serializer_class = ProUserSerializer
    permission_classes = [IsAuthenticated]


class ProRestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API View for retrieving, updating, or deleting a ProRestaurant instance by its ID.

    Permissions:
        - Authenticated users only (IsAuthenticated)

    Path Parameters:
        - id: The ID of the ProRestaurant to be retrieved, updated, or deleted.

    Responses:
        - 200: The ProRestaurant object is returned for retrieval.
        - 204: No content returned for successful deletion.
        - 404: ProRestaurant instance does not exist.
        - 403: User is not authenticated for the operation.
    """
    queryset = ProRestaurant.objects.all()
    serializer_class = ProRestaurantSerializer
    permission_classes = [IsAuthenticated]

