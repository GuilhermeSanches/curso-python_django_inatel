from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=128, unique=True)

class Driver(models.Model):
    name = models.CharField(max_length=128)

class Vehicle(models.Model):    
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    license_plate = models.CharField(max_length=7)
    manufacture_year = models.DateField()
    is_active = models.BooleanField(default=True)
    usecontrols = models.ManyToManyField(Driver, through="UseControl")
    manufacturer = models.ForeignKey("Manufacturer")

class UseControl(models.Model):
    driver = models.ForeignKey(Driver)
    vehicle = models.ForeignKey(Vehicle)
    date_started = models.DateField(auto_now_add=True)
    date_ended = models.DateField(blank=True, null=True)
