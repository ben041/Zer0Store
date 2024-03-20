from distutils.command.upload import upload
from email.mime import image
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    new_price = models.DecimalField(max_digits=10, decimal_places=2, default=100)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.name


class Doctors(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.name
