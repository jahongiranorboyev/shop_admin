# forms.py
from django import forms
from .models import Product
from apps.categories.models import Category, Subcategory, Brand

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'subcategory', 'brand', 'product_type', 'unit', 'images', 'thumbnail_image', 'video_link', 'video_provider', 'weight', 'dimensions_length', 'dimensions_width', 'dimensions_height']

    # Optionally add custom validations here
    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation if needed
        return cleaned_data
