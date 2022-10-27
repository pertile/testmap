from django.contrib.gis.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    home_address = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    location = models.PointField()
    
    def __str__(self):
        return str(self.user)