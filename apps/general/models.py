from django.db import models

from apps.utils.models.base_model import AbstractBaseModel


# Create your models here.
class General(AbstractBaseModel):
    name = models.CharField(max_length=100)


class PaymentMethod(AbstractBaseModel):
    """
    Represents a payment method available in the system.

    Attributes:
        name (str): The name of the payment method.
    """
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
