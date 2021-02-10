from django.db import models
from django.contrib.auth.models import User

class UserImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars', blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username