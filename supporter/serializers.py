from rest_framework import serializers
from .models import *


class QSerilazers(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = "__all__"

    def get_answers(self,obj):
        r = obj.answers.all()
        return ASerilazers(instance=r,many=True).data


class ASerilazers(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["answer"]
