from django import forms

from .models import Formula
# Create your tests here.

class MyFormula(forms.ModelForm):
    class Meta:
        model = Formula
