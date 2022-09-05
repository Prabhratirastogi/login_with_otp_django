from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Profile(AbstractUser):
    username = models.CharField(max_length=50, blank=True,null=True,unique=True)
    mobile = models.CharField(max_length=20)
    otp = models.CharField(max_length=6)
    
    
    