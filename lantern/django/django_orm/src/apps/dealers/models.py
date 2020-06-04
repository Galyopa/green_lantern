from django.db import models


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=32, unique=True)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=64)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Dealer(models.Model):  # унаследовать от юзера
    title = models.CharField(max_length=255)
    email = models.EmailField(max_length=64, unique=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
