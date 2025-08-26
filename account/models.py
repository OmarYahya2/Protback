from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    message = models.TextField( blank=True, null=True) 
    
    def __str__(self):
        return self.name
