from django.db import models
from django.contrib.auth.models import User


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


class Dealer(User):
    title = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)


class NewsLetter(models.Model):
    email = models.EmailField(max_length=64, unique=True)
