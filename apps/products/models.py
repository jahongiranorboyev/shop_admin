from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify

from apps.utils.models.base_model import AbstractBaseModel


class Product(AbstractBaseModel):
    """
    Represents a product in the system.
    """
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=100, blank=True)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='category_products',
                                 blank=True, null=True)
    brand = models.ForeignKey('brands.Brand', on_delete=models.CASCADE, blank=True, null=True)
    product_type = models.CharField(max_length=100, choices=[('Simple', 'Simple'), ('Classified', 'Classified')])
    unit = models.CharField(max_length=100, choices=[('Kilogram', 'Kilogram'), ('Pieces', 'Pieces')])

    slug = models.SlugField(unique=True, editable=False)
    images = models.ImageField(upload_to='products/images/%Y/%m/%d/', null=True, blank=True)
    thumbnail_image = models.ImageField(upload_to='product/images/%Y/%m/%d/', null=True, blank=True)
    video_link = models.URLField(blank=True, null=True)
    video_provider = models.CharField(max_length=100, choices=[('Vimeo', 'Vimeo'), ('Youtube', 'Youtube'),
                                                               ('Dailymotion', 'Dailymotion')], blank=True, null=True)

    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dimensions_length = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dimensions_width = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dimensions_height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def clean(self):
        """
        Ensure that the slug is created for the product and is unique.
        """

        if not self.slug:
            self.slug = slugify(self.name)

        if Product.objects.exclude(pk=self.pk).filter(slug=self.slug).exists():
            raise ValidationError({'slug': 'A product with this slug already exists.'})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
