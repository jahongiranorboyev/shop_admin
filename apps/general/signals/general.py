from django.core.exceptions import FieldDoesNotExist
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models

from apps.utils.services.normalize_text import *


@receiver(pre_save)
def general_pre_save(instance, *args, **kwargs):
    for field in instance._meta.get_fields():
        # If the field is a text type (CharField or TextField)
        if isinstance(field, (models.CharField, models.TextField)):
            field_name = field.name
            try:
                value = getattr(instance, field_name)
                # Normalize text
                if value:
                    normalized_value = normalize_text(value)
                    setattr(instance, field_name, normalized_value)
            except FieldDoesNotExist:
                continue
