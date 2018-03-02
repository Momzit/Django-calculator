from django import forms
from .models import Input

class Inputform(forms.ModelForm):
    class Meta:
        model = Input
        # exclude = ['monthly_payments']
        fields = '__all__'
