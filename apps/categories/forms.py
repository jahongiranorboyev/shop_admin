from django import forms
from .models import Category, Brand

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image', 'parent']  # You can add more fields if necessary


