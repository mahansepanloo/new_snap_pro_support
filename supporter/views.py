from supporter.models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *

class Q_and_A_list(ListAPIView):
    queryset = Q_and_A.objects.all()
    serializer_class = Q_and_A_serializer

class Q_and_A_(CreateAPIView):
    queryset = Q_and_A.objects.all()
    serializer_class = Q_and_A_serializer

class Q_and_A_update(UpdateAPIView):
    queryset = Q_and_A.objects.all()
    serializer_class = Q_and_A_serializer

class Q_and_A_delete(DestroyAPIView):
    queryset = Q_and_A.objects.all()
    serializer_class = Q_and_A_serializer

class Q_and_A_detail(RetrieveAPIView):
    queryset = Q_and_A.objects.all()
    serializer_class = Q_and_A_serializer