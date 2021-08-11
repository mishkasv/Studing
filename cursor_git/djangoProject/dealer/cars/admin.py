from django.contrib import admin
from .models import Car, Color, Model_car, Brand, Picture, FuelType

admin.site.register(Car)
admin.site.register(Color)
admin.site.register(Model_car)
admin.site.register(Brand)
admin.site.register(Picture)
admin.site.register(FuelType)

# Register your models here.
