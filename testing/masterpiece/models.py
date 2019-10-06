from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Masterpiece(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(
        decimal_places=2,
        max_digits=15
    )

    def get_absolute_url(self):
        return reverse('list')

class Buyer(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    nationality = models.CharField(max_length=30)
    property = models.CharField(max_length=30)
    gender = models.CharField(max_length=5, null=True)