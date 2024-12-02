from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.utils.models.base_model import AbstractBaseModel
from django.db import models


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
        if Brand.objects.exclude(pk=self.pk).filter(name=self.name).exists():
            raise ValidationError({'name': _('Brand name already exists')})
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
