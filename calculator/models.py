from django.db import models

# Create your models here.
from django.urls import reverse

class Input(models.Model):

    name_to_save = models.CharField(max_length=500, default='Results')
    purchase_price = models.DecimalField(max_digits=19, decimal_places=2, default=100000)
    deposit_paid = models.DecimalField(max_digits=19, decimal_places=2, default=50000)
    bond_term = models.DecimalField(max_digits=19, decimal_places=2, default=2)
    fixed_interest_rate = models.DecimalField(max_digits=19, decimal_places=2, default=0.1)

    def __str__(self):
        return self.name_to_save

    def total(self):
        A = self.purchase_price - self.deposit_paid 
        r = (self.fixed_interest_rate/100)
        n = 12
        numerator = A*(r/n)
        denomenator = 1 - (1 + (r/n))**(-n*self.bond_term)
        mortgage = (numerator/denomenator)
        return 'R' + '{0:.2f}'.format(mortgage)
