from rest_framework.serializers import ModelSerializer
from .models import Q_and_A


class Q_and_A_serializer(ModelSerializer):
    class Meta:
        model = Q_and_A
        fields = '__all__'

