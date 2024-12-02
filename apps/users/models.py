from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from apps.utils.models.base_model import AbstractBaseModel
from apps.utils.models.regions import Region
from apps.utils.models.districts import District

class CustomUser(AbstractBaseModel, AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT, null=True)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.username

