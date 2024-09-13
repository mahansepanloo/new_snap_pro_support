from django.db import models

class Subscription(models.Model):
    TYPE_CHOICES = [
        (1, 'Monthly'),
        (3, 'Quarterly'),
        (6, 'Semi-Annual'),
    ]

    TITLE_CHOICES = [
        ('Monthly Subscription', 'Monthly Subscription'),
        ('Quarterly Subscription', 'Quarterly Subscription'),
        ('Semi-Annual Subscription', 'Semi-Annual Subscription'),
    ]

    PRICE_CHOICES = [
        (100000, '100,000'),
        (270000, '270,000'),
        (500000, '500,000'),
    ]

    title = models.CharField(max_length=500, choices=TITLE_CHOICES)
    price = models.BigIntegerField(choices=PRICE_CHOICES)
    subscription_type = models.IntegerField(choices=TYPE_CHOICES)



    def __str__(self):
        return f"{self.title} - {self.price}"

class SubscriptionRestaurant(models.Model):
    TYPE_CHOICES = [
        (3, 'Quarterly'),
        (6, 'Semi-Annual'),
        (12, 'Annual'),
    ]

    TITLE_CHOICES = [
        ('Annual Subscription', 'Annual Subscription'),
        ('Quarterly Subscription', 'Quarterly Subscription'),
        ('Semi-Annual Subscription', 'Semi-Annual Subscription'),
    ]

    PRICE_CHOICES = [
        (5000000, '5,000,000'),
        (9000000, '9,000,000'),
        (13000000, '13,000,000'),
    ]

    title = models.CharField(max_length=500, choices=TITLE_CHOICES)
    price = models.BigIntegerField(choices=PRICE_CHOICES)
    subscription_type = models.IntegerField(choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.title} - {self.price}"