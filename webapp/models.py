from django.db import models

# Create your models here.
class customercontactdb(models.Model):
    CONTACTNAME = models.CharField(max_length=100, null=True, blank=True)
    CONTACTNUMBER = models.IntegerField(max_length=100, null=True, blank=True)
    CONTACTEMAIL=models.EmailField(max_length=100,null=True,blank=True)
    CONTACTSUBJECT=models.CharField(max_length=100,null=True,blank=True)
    CONTACTMESSAGE=models.CharField(max_length=100,null=True,blank=True)


class bookingdb(models.Model):
    CUSTOMERNAME = models.CharField(max_length=100, null=True, blank=True)
    CONTACTEMAIL = models.EmailField(max_length=100, null=True, blank=True)
    CHECKIN = models.CharField(max_length=100, null=True, blank=True)
    CHECKOUT = models.CharField(max_length=100, null=True, blank=True)
    TOTALADULTS = models.CharField(max_length=100, null=True, blank=True)
    TOTALCHILDS = models.IntegerField(max_length=100, null=True, blank=True)
    SELECTROOM = models.CharField(max_length=100, null=True, blank=True)
    SPECIALREQUEST = models.CharField(max_length=100, null=True, blank=True)
    TOTALPRICE = models.IntegerField(null=True, blank=True)

class Registerdb(models.Model):
    USERNAME=models.CharField(max_length=100,null=True,blank=True)
    PASSWORD=models.CharField(max_length=100,null=True,blank=True)
    CONFIRMPASSWORD=models.CharField(max_length=100,null=True,blank=True)
    EMAIL=models.CharField(max_length=100,null=True,blank=True)
class Totaldb(models.Model):
    CUSTOMERNAME=models.CharField(max_length=100,null=True,blank=True)
    MOBILE=models.IntegerField(null=True,blank=True)
    TOTALPRICE=models.IntegerField(null=True,blank=True)



