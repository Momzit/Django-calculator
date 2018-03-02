from django.db import models

# Create your models here.
from django.urls import reverse

class Input(models.Model):

    name_to_save = models.CharField(max_length=500, default='Results')
    purchase_price = models.DecimalField(max_digits=19, decimal_places=2, default=None)
    deposit_paid = models.DecimalField(max_digits=19, decimal_places=2, default=None)
    bond_term = models.DecimalField(max_digits=19, decimal_places=2, default=None)
    fixed_interest_rate = models.DecimalField(max_digits=19, decimal_places=2, default=None)

    def __str__(self):
        return self.name_to_save
