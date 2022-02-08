from django.db import models

# Create your models here.
class StudntRegistration(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    department = models.CharField(max_length=23)
    mobno= models.IntegerField()