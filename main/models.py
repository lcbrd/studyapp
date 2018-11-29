from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    
# Create your models here.