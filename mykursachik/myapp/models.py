from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.

class Director(models.Model):
     name = models.CharField(max_length=100)
     details = models.CharField(max_length=500)
     age = models.IntegerField()
     experience = models.IntegerField()
     isCreep = models.BooleanField()
     def __unicode__(self):
         return self.name 

class Ad(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    mark = models.IntegerField()
    price = models.IntegerField()
    director = models.ForeignKey(Director, on_delete = models.PROTECT)
    user = models.ForeignKey(User, on_delete = models.PROTECT)

class Method(models.Model):
    v1_order = models.IntegerField()
    v1_mark = models.IntegerField()
    v2_order = models.IntegerField()
    v2_mark = models.IntegerField()
    v3_order = models.IntegerField()
    v3_mark = models.IntegerField()








   




    

    