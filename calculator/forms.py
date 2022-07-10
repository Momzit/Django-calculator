from django import forms
from .models import Input

class Inputform(forms.ModelForm):
    class Meta:
        model = Input
        # exclude = ['monthly_payments']
        fields = '__all__'
        widgets = {
            'name_to_save': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Filename...'}),
            'purchase_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g 100000'}),
            'deposit_paid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g 50000'}),
            'bond_term': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g 2 (in years)'}),
            'fixed_interest_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g 10 (as a percentage)'}),
        }
