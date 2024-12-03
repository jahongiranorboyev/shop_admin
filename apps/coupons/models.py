from django.db import models
from django.utils import timezone

from apps.utils.models.base_model import AbstractBaseModel


class Coupon(AbstractBaseModel):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=100, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

    def is_active(self):
        # Check if the current date is between the start_date and end_date
        now = timezone.now().date()
        return self.start_date <= now <= self.end_date
