from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
    )
    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
    )
    image = models.ImageField(upload_to='food')
    def __str__(self):
        return self.name


class Menu(models.Model):
    DEFAULT_MENU = 'default'
    FALL = 'fall'
    SPRING = 'spring'
    SUMMER = 'summer'
    WINTER = 'winter'
    HELLOWEEN = 'helloween'
    CRISTMAS = 'cristmas'

    SEASONS_EVENTS = (
        (DEFAULT_MENU, 'Стандартне'),
        (FALL, 'осінь'),
        (SUMMER, 'літо'),
        (SPRING, 'весна'),
        (WINTER, 'зима'),
        (HELLOWEEN, 'хелоуін'),
        (CRISTMAS, 'різдво'),
    )
    title = models.CharField(max_length=50, default='default')
    foods = models.ManyToManyField(
        Food,
        related_name='menus',
    )
    season = models.CharField(max_length=50, choices=SEASONS_EVENTS, default=DEFAULT_MENU)

    def __str__(self):
        return self.title


class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
    )
    county = models.ForeignKey(
        Country,
        on_delete=models.DO_NOTHING,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.DO_NOTHING,
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='menu',
    )
    def __str__(self):
        return self.name


class Personal(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    work = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='worker'
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.DO_NOTHING,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.DO_NOTHING,
    )
    def __str__(self):
        return self.first_name + ' ' + self.last_name
