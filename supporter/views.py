
from rest_framework import generics
from .serializers import *
from .permissions import Is_supporterPermisions


class CreateQ(generics.ListCreateAPIView):
   queryset = Question.objects.all()
   serializer_class = QSerilazers

class CreateAnser(generics.ListCreateAPIView):
   queryset = Answer.objects.all()
   serializer_class = ASerilazers
   permission_classes = [Is_supporterPermisions]

   def perform_create(self, serializer):



      question_id = self.request.data["id_q"]
      question = Question.objects.get(id=int(question_id))
      answer_instance = Answer.objects.create(question=question,supporter=self.request.user,answer=serializer.validated_data.get("answer"))
      question.status = True
      question.save()

      return answer_instance







