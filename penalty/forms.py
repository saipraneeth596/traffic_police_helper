from django.core import validators
from django import forms
from .models import violation

class addfine(forms.ModelForm):
    class Meta:
        model = violation
        fields =['vehicle_number','violation_done','fine_amt']
        widgets= {
            'vehicle_number': forms.TextInput(attrs={'class' : 'form-control'}),
            'fine_amt': forms.NumberInput(attrs={'class': 'form-control'}),
            'finereason': forms.TextInput(attrs={'class': 'form-control'})
        }


