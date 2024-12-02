from django.contrib import admin
from django.utils.text import slugify

from apps.brands.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    prepopulated_fields = {'slug': ('name',)}  # Automatically generate slug from name

    def save_model(self, request, obj, form, change):
        """
        Custom save method to automatically generate the slug before saving.
        """
        if not obj.slug:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)
