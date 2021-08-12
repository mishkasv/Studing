from django.db import models


class Property(models.Model):
    category = models.CharField(max_length=120)
    name = models.CharField(max_length=50)
    carproperty = models.ManyToManyField(
        'cars.Car',
        related_name='carpropery',
    )

    def __str__(self):
        return self.name
