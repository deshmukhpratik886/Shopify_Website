from django.core import validators
from django import forms
from .models import User


class Shopify_Inventory(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Item_name','Total_Stock_In_KG','Price_Per_KG']
        widgets = {
            'Item_name': forms.TextInput(attrs={'class':'form-control'}),
            'Total_Stock_In_KG': forms.NumberInput(attrs={'class':'form-control'}),
            'Price_Per_KG':forms.NumberInput(attrs={'class':'form-control'}),

        }

