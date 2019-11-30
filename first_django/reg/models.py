from django.db import models

class Reg(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
  

    def _str_(self):
        return self.email