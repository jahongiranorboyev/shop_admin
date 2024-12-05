from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.core.cache import cache

from apps.utils.models.base_model import AbstractBaseModel
from apps.utils.models.regions import Region
from apps.utils.models.districts import District


class CustomUser(AbstractBaseModel, AbstractUser):
    USER_PERMISSION_CACHE_KEY = 'permission_user_{}'
    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT, blank=True, null=True)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def has_perm(self, perm, obj=None):
        permissions = cache.get(self.USER_PERMISSION_CACHE_KEY.format(self.pk))
        if permissions is None:
            permissions = self.get_all_permissions(obj=obj)
            cache.set(self.USER_PERMISSION_CACHE_KEY.format(self.pk), permissions)
        return perm in permissions

    def save(self, *args, **kwargs):
        cache.delete(self.USER_PERMISSION_CACHE_KEY.format(self.pk))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
