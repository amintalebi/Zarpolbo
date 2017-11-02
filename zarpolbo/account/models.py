from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(to=User, related_name='profile')
    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username


