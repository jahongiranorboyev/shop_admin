from django.views.generic import ListView

from django.shortcuts import render
from django.views.generic import CreateView

from apps.coupons.models import Coupon


class CouponListView(ListView):
    model = Coupon
    template_name = 'pages/coupon-list.html'

class CreateCouponView(CreateView):
    model = Coupon
    template_name = 'pages/create-coupon.html'