from django.db import models

# Create your models here.
from django.db import models

class Bus(models.Model):
    bus_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('Available', 'Available'), ('In-Service', 'In-Service')])
    route = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.bus_number} - {self.status}'

class Route(models.Model):
    route_name = models.CharField(max_length=50, unique=True)
    total_stops = models.IntegerField()

    def __str__(self):
        return self.route_name

class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
