from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profilePhoto = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    backgroundPhoto = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return self.user.username