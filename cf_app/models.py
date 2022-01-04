from django.db import models

# Create your models here.


class Cars(models.Model):
    mileage = models.IntegerField(default=0)
    year_of_manufacture = models.IntegerField(default=0)
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    fuel_efficiency = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return f"{self.year_of_manufacture} {self.manufacturer} {self.model}"