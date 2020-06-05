from django.db import models
from django.db.models import Index
from phone_field import PhoneField
from common.models import BaseDateAuditModel
from django.utils.translation import gettext_lazy as _


class Order(BaseDateAuditModel):
    STATUS_PAID = 'paid'
    STATUS_DEPOSIT_PAID = 'deposit paid'
    STATUS_ARCHIVED = 'archived'
    STATUS_EXPECT_PAYMENT = 'expect payment'

    STATUS_CHOICES = (
        (STATUS_PAID, "Paid"),
        (STATUS_DEPOSIT_PAID, "Deposit paid"),
        (STATUS_ARCHIVED, "Archived"),
        (STATUS_EXPECT_PAYMENT, "Expect payment"),
    )

    car = models.ForeignKey(to='cars.Car', on_delete=models.DO_NOTHING, null=True, blank=False)
    views = models.PositiveIntegerField(default=0, editable=False)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_EXPECT_PAYMENT, blank=True)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=64, unique=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    message = models.CharField(max_length=32)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

        indexes = [
            Index(fields=['status', ])
        ]




