from django.db import models
from rest_framework import  viewsets
import uuid

# Create your models here.
class Customers(models.Model):
    id = models.UUIDField(primary_key= True, editable=False ,default=uuid.uuid4)
    name = models.CharField(max_length=30)
    age = models.IntegerField(max_length=3)
    orders = models.CharField()


    def __str__(self):
        return self.name

