from django.db import models

# Create your models here.


class Cafe(models.Model):
    cafe_name = models.CharField(max_length=200)
