from django import forms
from .models import Contacto, Productos


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ["name", "email", "mensaje"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ["name", "description", "stock", "imagen"]
