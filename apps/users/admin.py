from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
        ('Personal info', {'fields': ('full_name', 'phone_number', 'region', 'district')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )


    readonly_fields = ('last_login', 'date_joined')


    list_display = ('username', 'email', 'full_name', 'is_active', 'is_staff')
