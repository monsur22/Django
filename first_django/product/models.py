from django.db import models
from django import forms
# Create your models here.
class Category(models.Model):
    c_name = models.CharField(max_length=50)


    def _str_(self):
        return self.c_name

class Product(models.Model):
    p_name = models.CharField(max_length=255)
    p_desc = models.TextField()
    p_price = models.CharField(max_length=255)
    p_date=models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    p_c_name = models.ForeignKey(Category, on_delete=True)
    image = models.ImageField()
    # image = models.ImageField(upload_to='images/')



    def __str__(self):
        return self.p_name