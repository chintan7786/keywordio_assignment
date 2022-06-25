from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.book_name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username