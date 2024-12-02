from django.conf import settings
from django.db import models

from apps.utils.models.base_model import AbstractBaseModel


class Role(AbstractBaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Permission(AbstractBaseModel):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class UserRole(AbstractBaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'role')

    def __str__(self):
        return {self.role.name}

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('role', 'permission')

    def __str__(self):
        return f"{self.role.name} - {self.permission.title}"




