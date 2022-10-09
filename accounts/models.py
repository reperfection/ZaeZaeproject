from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    introduce = models.CharField(max_length=255, null=True, blank=True)
    userphoto= models.ImageField(upload_to='images/', blank=True, null=True)
    