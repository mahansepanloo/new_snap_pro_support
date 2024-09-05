from django.db import models
from django.contrib.auth.models import User
from accounts.models import Pro_user,Pro_restuarant
class Q_and_A(models.Model):
    supprter = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    text = models.TextField()
    answer = models.TextField(Null= True , blank=True)
    status = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(Null = True , blank=True)




