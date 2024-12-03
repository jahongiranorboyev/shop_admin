from django.contrib import admin
from .models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'start_date', 'end_date', 'discount_percent')
    search_fields = ('title', 'code')
