from django.db import models

# Create your models here.
class OrderList(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    other = models.CharField(max_length=50)

