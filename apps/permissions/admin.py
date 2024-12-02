from django.contrib import admin
from django.contrib import admin
from .models import Role, Permission, UserRole, RolePermission

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')

@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ('role', 'permission')
