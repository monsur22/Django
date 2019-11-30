from django.db import models

class Account(models.Model):  
    fname = models.CharField(max_length=20)  
    lname = models.CharField(max_length=100)  
    email = models.EmailField()  
    password = models.CharField(max_length=200)  
    class Meta:  
        db_table = "account"  

class Verifyaccount(models.Model):  
    fname = models.CharField(max_length=100,null=True)  
    lname = models.CharField(max_length=100,null=True)  
    email = models.EmailField(max_length=200,null=True)  
    token = models.CharField(max_length=200,null=True)  
    password = models.CharField(max_length=200,null=True)  
    class Meta:  
        db_table = "verifyaccount" 