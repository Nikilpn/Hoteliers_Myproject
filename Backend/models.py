from django.db import models

# Create your models here.
class roomtypedb(models.Model):
    ROOMTYPE=models.CharField(max_length=100,null=True,blank=True)
    ROOMTYPEIMAGE=models.ImageField(upload_to="roomtypeimages",null=True,blank=True)
    DESCRIPTION = models.CharField(max_length=100, null=True, blank=True)

#
class roomnamedb(models.Model):
    ROOMTYPE = models.CharField(max_length=100, null=True, blank=True)
    ROOMNAME=models.CharField(max_length=100,null=True,blank=True)
    ROOMIMAGE=models.ImageField(upload_to="roomimage",null=True,blank=True)
    ROOMPRICE=models.IntegerField(null=True,blank=True)
    ROOMDESCRIPTION=models.CharField(max_length=100,null=True,blank=True)

class staffdb(models.Model):
    STAFFNAME = models.CharField(max_length=100, null=True, blank=True)
    STAFFDESIGNATION=models.CharField(max_length=100,null=True,blank=True)
    STAFFACEBOOK=models.CharField(max_length=100,null=True,blank=True)
    STAFFINSTA=models.CharField(max_length=100,null=True,blank=True)
    STAFFIMAGE=models.ImageField(upload_to="staffimage",null=True,blank=True)
