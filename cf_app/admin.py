from django.contrib import admin
from .models import Car, CarYear, CarMake, CarModel
# Register your models here.
admin.site.register(Car)
admin.site.register(CarYear)
admin.site.register(CarMake)
admin.site.register(CarModel)