from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'desc', 'price', 'thumbnail', 'category', 'active']

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'desc': forms.Textarea(attrs={'class': 'form-control'}),
        'price': forms.NumberInput(attrs={'class': 'form-control'}),
        'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
        'category': forms.Select(attrs={'class': 'form-control'}),
        'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }

    class CategoryChoiceField(forms.ModelChoiceField):
        def label_from_instance(self, obj):
            return obj.name

    # Sử dụng lớp con trong trường category
    category = CategoryChoiceField(queryset=Category.objects.all())

class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address', 'city', 'stay', 'phone']

        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'stay': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }