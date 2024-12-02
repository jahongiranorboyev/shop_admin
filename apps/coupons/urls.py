from django.urls import path

from apps.coupons.views import CouponListView, CreateCouponView
app_name = 'coupons'
urlpatterns = [
    path('', CouponListView.as_view(), name='coupon_list'),
    path('create-coupon/',CreateCouponView.as_view(), name='create_coupon'),

]