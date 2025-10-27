from django.db import models

class Book(models.Model):

    class Cover(models.TextChoices):
        HARD = "Hard"
        SOFT = "Soft"

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover = models.IntegerField(choices=Cover.choices, default=None)
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=10, decimal_places=2)
