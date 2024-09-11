from django.db import models

class Subscription(models.Model):
    TYPE_CHOICES = [
        (1, 'Monthly'),
        (3, 'Quarterly'),
        (6, 'Semi-Annual'),
    ]
    title = models.CharField(max_length=500)
    price = models.BigIntegerField()
    subscription_type = models.IntegerField(choices=TYPE_CHOICES)
