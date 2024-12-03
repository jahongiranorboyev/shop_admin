from django.urls import path

from apps.coupons.views import CouponListView, CouponCreateView, CouponUpdateView, CouponDeleteView

app_name = 'coupons'
urlpatterns = [
    path('', CouponListView.as_view(), name='coupon_list'),
    path('coupon-create/',CouponCreateView.as_view(), name='create_coupon'),
    path('coupon-edit/<uuid:pk>/', CouponUpdateView.as_view(), name='edit_coupon'),
    path('coupon-delete/<uuid:pk>/', CouponDeleteView.as_view(), name='delete_coupon'),

]