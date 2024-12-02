from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from apps.utils.models.base_model import AbstractBaseModel


class Category(AbstractBaseModel):
    """
    Represents a product category in the system.
    """
    name = models.CharField(
        max_length=255,
        help_text="The name of the category."
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        editable=False,
    )
    image = models.ImageField(
        upload_to='category/images/%Y/%m/%d/',
        null=True,
        blank=True,
        help_text="An optional image representing the category."
    )
    parent = models.ForeignKey(
        to='self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children',
        related_query_name='category',
        help_text="The parent category for nested categories (optional)."
    )

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def clean(self):
        """
        Custom validation to ensure categories have no more than two levels.
        """
        try:
            if not self.pk and self.parent and self.parent.parent:
                raise ValidationError("You can create only two levels of categories.")
        except AttributeError:
            pass

        self.slug = slugify(self.name)
        if Category.objects.exclude(pk=self.pk).filter(slug=self.slug).exists():
            raise ValidationError({'name': _('Name already exists')})

    def __str__(self):
        return self.name


class Subcategory(Category):
    """
    Represents a product subcategory in the system, inheriting from Category.
    """
    class Meta:
        verbose_name_plural = "Subcategories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Brand(AbstractBaseModel):
    """
    Represents a brand of products in the system.
    """
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    class Meta:
        verbose_name_plural = "Brands"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if  Brand.objects.exclude(pk=self.pk).filter(name=self.name).exists():
            raise ValidationError({'name': _('Brand name already exists')})
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



