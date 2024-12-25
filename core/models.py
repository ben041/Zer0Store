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
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional field for phone
    email = models.EmailField(blank=True, null=True)  # Optional email field
    address = models.TextField(max_length=300, blank=True, null=True)  # Optional address field
    specialization = models.CharField(max_length=100, blank=True, null=True)  # Optional specialization field

    def __str__(self):
        return self.name
