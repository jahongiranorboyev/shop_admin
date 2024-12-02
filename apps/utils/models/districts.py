from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.utils.models.base_model import AbstractBaseModel
from apps.utils.models.regions import Region

class District(AbstractBaseModel):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(to=Region, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    def clean(self):
        self.slug = slugify(self.name)
        if District.objects.exclude(pk=self.pk).filter(slug=self.slug).exists():
            raise ValidationError({'name': _('Name already exists')})

    class Meta:
        db_table = 'districts'
        verbose_name = _("District")
        verbose_name_plural = _("District")
        ordering = ['name']