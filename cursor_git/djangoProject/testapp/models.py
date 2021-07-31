from django.db import models

class Country(models.Model):
    name=models.CharField(max_length=100)
    code = models.IntegerField()
    pass


class City(models.Model):
    name=models.CharField(max_length=100)
    county = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='country_of_city'
    )
    pass



class Food(models.Model):
    name=models.CharField(max_length=100)
    county = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='country_of_food',
        null=True,
    )
    image = models.ImageField(upload_to='food')
    pass


class Menu(models.Model):
    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        related_name='food'
    )
    pass


class Restaurant(models.Model):
    name=models.CharField(
        max_length=100,
    )
    county = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='country_of_rest'
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='city_of_rest'
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='menu',
    )

    pass

class Personal(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=20)
    work=models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='restaurant'
    )
    country=models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='country_of_person'
    )
    city=models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='city_of_person'
    )
    pass