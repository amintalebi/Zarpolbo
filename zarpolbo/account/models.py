from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(to=User, related_name='informations')
    user_name = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    pass_word = models.CharField(max_length=50, null=False, blank=False)
    email_address = models.EmailField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.user.username