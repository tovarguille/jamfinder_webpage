from django.db import models
from django.contrib.auth.models import User

class Local(models.Model):
    name = models.CharField(max_length=100)
    type_of_studio = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    opening_hours = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    services = models.CharField(max_length=300, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre
