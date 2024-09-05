from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    user = models.CharField(max_length=5000)
    text = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    supporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField()

    def __str__(self):
        return self.answer[:50]
