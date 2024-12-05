from django.utils.text import slugify

from apps.products.models import Product
from django.contrib import admin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'price', 'category','brand', 'slug', 'created_at', 'updated_at'
    )
    search_fields = ('name',)
    list_filter = ('category', 'brand')
    prepopulated_fields = {'slug': ('name',)}  # Automatically generate slug from name

    def save_model(self, request, obj, form, change):
        """
        Custom save method to automatically generate the slug before saving.
        """
        if not obj.slug:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)

