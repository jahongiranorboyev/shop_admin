from django.contrib import admin
from apps.reports.models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_price', 'created_at']
    search_fields = ['total_price']
    list_filter = ['created_at']
    ordering = ['-created_at']
