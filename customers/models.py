from django.db import models
from rest_framework import  viewsets

# Create your models here.
class Customers(models.Model):
    id = models.UUIDField(primary_key= True, editable=False ,null=False,blank=False)
    name = models.CharField(max_length=30)
    age = models.IntegerField(max_length=3)
    orders = models.CharField()

