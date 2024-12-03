from django.contrib import admin
from .models import Category
from django.utils.text import slugify

# Admin for Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('parent',)
    prepopulated_fields = {'slug': ('name',)}  # Automatically generate slug from name

    def save_model(self, request, obj, form, change):
        """
        Custom save method to automatically generate the slug before saving.
        """
        if not obj.slug:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)


