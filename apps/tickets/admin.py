from django.contrib import admin
from apps.tickets.models import Ticket  # Ticket modelini import qiling


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'status', 'created_at']
    search_fields = ['user__username', 'subject', 'comment']
    list_filter = ['status', 'created_at']
    ordering = ['-created_at']
    readonly_fields = ['created_at']

