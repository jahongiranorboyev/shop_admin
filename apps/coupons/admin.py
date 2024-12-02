from django.contrib import admin
from apps.coupons.models import Coupon, CouponRestriction, CouponUsage


class CouponRestrictionInline(admin.TabularInline):
    model = CouponRestriction
    extra = 1


class CouponUsageInline(admin.TabularInline):
    model = CouponUsage
    extra = 1


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'start_date', 'end_date', 'free_shipping', 'status')
    list_filter = ('status', 'free_shipping', 'start_date', 'end_date')
    search_fields = ('title', 'code')
    ordering = ('-start_date',)
    inlines = [CouponRestrictionInline, CouponUsageInline]


@admin.register(CouponRestriction)
class CouponRestrictionAdmin(admin.ModelAdmin):
    list_display = ('coupon', 'products', 'category', 'minimum_spend', 'maximum_spend')
    search_fields = ('coupon__title','category__name')
    list_filter = ('category',)  #


@admin.register(CouponUsage)
class CouponUsageAdmin(admin.ModelAdmin):
    list_display = ('coupon', 'per_limited', 'per_customer')
    search_fields = ('coupon__title',)
