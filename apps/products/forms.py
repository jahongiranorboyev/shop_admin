# forms.py
from django import forms
from .models import Product
from apps.brands.models import Brand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'name', 'price', 'description', 'category',
             'brand', 'product_type', 'unit',
            'images', 'thumbnail_image', 'video_link',
            'video_provider', 'weight', 'dimensions_length',
            'dimensions_width', 'dimensions_height',
        ]


    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), required=False)

