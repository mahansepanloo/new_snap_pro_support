from django.db import models
from django.contrib.auth.models import User

class Pro_user(models.Model):
    user = models.OneToOneField(User, on_delete=False)
    is_pro = models.BooleanField(default=False)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField()

    def __str__(self):
        return self.user.username

class Pro_restuarant(models.Model):
    user = models.OneToOneField(User, on_delete=False)
    name = models.CharField(max_length=100)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField()
    def __str__(self):
        return self.user.username
