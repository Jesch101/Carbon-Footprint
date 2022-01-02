from django.db import models
from django.urls import reverse
# Create your models here.


class CarYear(models.Model):
    year = models.IntegerField(default=0)
    def __str__(self):
        return str(self.year)

class CarMake(models.Model):
    year = models.ForeignKey(CarYear, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    
    def __str__(self):
        return self.name

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

class Car(models.Model):
    year = models.ForeignKey(CarYear, on_delete=models.SET_NULL, blank=True, null=True)
    make = models.ForeignKey(CarMake, on_delete=models.SET_NULL, blank=True, null=True)
    model = models.ForeignKey(CarModel, on_delete=models.SET_NULL, blank=True, null=True)

    fuel_efficiency = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"