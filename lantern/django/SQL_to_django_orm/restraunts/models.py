# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class City(models.Model):
    cityid = models.AutoField(primary_key=True)
    city = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    countryid = models.AutoField(primary_key=True)
    country = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Dish(models.Model):
    dishid = models.AutoField(primary_key=True)
    nameofdish = models.CharField(unique=True, max_length=30, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    class Meta:
        managed = False
        db_table = 'dish'


class Menu(models.Model):
    menudishid = models.AutoField(primary_key=True)
    dishid = models.ForeignKey(Dish, models.DO_NOTHING, db_column='dishid')

    class Meta:
        managed = False
        db_table = 'menu'


class Restaurant(models.Model):
    restaurantid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'


class Staff(models.Model):
    personid = models.AutoField(primary_key=True)
    firsname = models.CharField(max_length=40, blank=True, null=True)
    secondname = models.CharField(max_length=40, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    phone = models.CharField(unique=True, max_length=20)
    restaurantid = models.ForeignKey(Restaurant, models.DO_NOTHING, db_column='restaurantid')

    class Meta:
        managed = False
        db_table = 'staff'


class Summermenu(models.Model):
    summermenuid = models.AutoField(primary_key=True)
    dishid = models.ForeignKey(Dish, models.DO_NOTHING, db_column='dishid')

    class Meta:
        managed = False
        db_table = 'summermenu'
