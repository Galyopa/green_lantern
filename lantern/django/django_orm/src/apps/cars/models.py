from django.db import models
from django.db.models import Index, UniqueConstraint
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from apps.cars.managers import CarManager, CarQuerySet
from common.models import BaseDateAuditModel


class Color(models.Model):
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        indexes = [
            Index(fields=('name',))
        ]

        verbose_name = _('Color')
        verbose_name_plural = _('Colors')

    def __str__(self):
        return self.name


class CarBrand(models.Model):
    name = models.CharField(max_length=32, unique=True)
    logo = models.ImageField(null=True, blank=False)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',))
        ]
        verbose_name = _('Car brand')
        verbose_name_plural = _('Car brands')

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=64)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',)),
        ]
        verbose_name = _('Car model')
        verbose_name_plural = _('Car models')

    def __str__(self):
        return self.name


class Car(BaseDateAuditModel):
    STATUS_PENDING = 'pending'
    STATUS_PUBLISHED = 'published'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_SOLD, "Sold"),
        (STATUS_ARCHIVED, "Archived"),
    )

    objects = CarManager.from_queryset(CarQuerySet)()
    views = models.PositiveIntegerField(default=0, editable=False)
    slug = models.SlugField(max_length=75)
    number = models.CharField(max_length=16, unique=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_PENDING, blank=True)
    dealer = models.ForeignKey(to='dealers.Dealer', on_delete=models.CASCADE, related_name='cars')
    color = models.ForeignKey(to='Color', on_delete=models.SET_NULL, null=True, blank=False)
    model = models.ForeignKey(to='CarModel', on_delete=models.SET_NULL, null=True, blank=False)
    extra_title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Title second part'))
    engine_type = models.CharField(max_length=30, null=True, blank=True)
    population_type = models.CharField(max_length=255)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    fuel_type = models.CharField(max_length=30, null=True, blank=True)
    doors = models.PositiveSmallIntegerField(default=4)
    capacity = models.PositiveSmallIntegerField(default=4)
    gear_case = models.CharField(max_length=30, null=True, blank=True, default='automatic')
    sitting_place = models.PositiveSmallIntegerField(default=4)
    firs_registration_date = models.DateTimeField(auto_now_add=False)
    engine_power = models.DecimalField(max_digits=5, decimal_places=2)

    def save(self, *args, **kwargs):
        order_number_start = 7600000
        if not self.pk:
            super().save(*args, **kwargs)
            self.number = f"LK{order_number_start + self.pk}"
            self.save()
        else:
            super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.status = self.STATUS_ARCHIVED
        self.save()

    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')

        indexes = [
            Index(fields=['status', ])
        ]


class CarProperty(models.Model):
    property = models.ForeignKey(to='Property', on_delete=models.DO_NOTHING, null=True, blank=False)
    car = models.ForeignKey(to='Car', on_delete=models.DO_NOTHING, null=True, blank=False)


class Property(models.Model):
    category = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
