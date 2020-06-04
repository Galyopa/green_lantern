from django.db import models


class OrderQuerySet(models.QuerySet):
    def paid(self):
        return self.filter(status='paid')

    def deposit_paid(self):
        return self.filter(status='deposit paid')

    def archived(self):
        return self.filter(status='archived')

    def expect_payment(self):
        return self.filter(status='expect payment')
