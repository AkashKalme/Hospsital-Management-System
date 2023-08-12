from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
   name = models.CharField(max_length=300)
   gender = models.CharField(max_length=10)
   email = models.EmailField(null=True,blank=True)
   address = models.TextField(null=True,blank=True)
   date_of_Birth = models.DateField(null=True,blank=True)
   height = models.IntegerField(default=0)
   weight = models.IntegerField(default=0)
   reason = models.TextField(null=True,blank=True)
   notvisited = models.BooleanField(default=True)
   dateofvisit = models.DateTimeField(null=True,blank=True)

   def __str__(self):
    return self.name

class History(models.Model):
   patient = models.OneToOneField(Patient,on_delete=models.CASCADE)
   allergy = models.TextField(null=True,blank=True)
   dieases = models.TextField(null=True,blank=True)
   other = models.TextField(null=True,blank=True)
   operations = models.TextField(null=True,blank=True)
   currentmedications = models.TextField(null=True,blank=True)
   Exercise = models.CharField(null=True,blank=True,max_length=100)
   Eating = models.CharField(null=True,blank=True,max_length=100)
   Alcohol = models.CharField(null=True,blank=True,max_length=100)
   smoke = models.CharField(null=True,blank=True,max_length=100)
   Caffeine = models.CharField(null=True,blank=True,max_length=100)
   def __str__(self):
    return self.patient.name