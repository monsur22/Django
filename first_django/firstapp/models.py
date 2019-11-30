from django.db import models
from django import forms
# Create your models here.

class Firstapp(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)

    def _str_(self):
        return self.first_name