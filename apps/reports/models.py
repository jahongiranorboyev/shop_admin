from django.conf import settings
from django.db import models

from apps.utils.models.base_model import AbstractBaseModel


class Report(AbstractBaseModel):
    """
    Model for managing reports that summarize user transactions or activities.

    Fields:
        - user: A foreign key linking the report to a specific user.
        - total_price: The total monetary value related to the report (e.g., total spending or earnings).
        - created_at: The timestamp when the report was created.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)



