from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


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

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Dealer')
        verbose_name_plural = _('Dealers')
