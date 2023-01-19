from django.db import models


class Bank(models.Model):
    BANK_TYPE = [
        ('central bank', 'central bank'),
        ('commercial bank', 'commercial bank'),
        ('investment bank', 'investment bank'),
        ('savings bank', 'savings bank'),
        ('mortgage bank', 'mortgage bank'),
        ('special bank', 'special bank')
    ]
    name = models.CharField(max_length=128, blank=False, null=False)
    type = models.CharField(max_length=16, choices=BANK_TYPE, blank=False, null=False)
    number = models.CharField(max_length=6, blank=False, null=False)

    class Meta:
        db_table = "banks"


class PaymentSystem(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    number = models.CharField(max_length=2, blank=False, null=False)

    class Meta:
        db_table = "payment_systems"
