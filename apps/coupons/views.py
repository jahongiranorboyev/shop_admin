from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from .models import Coupon
from .forms import CouponForm


class CouponListView(PermissionRequiredMixin, ListView):
    permission_required = ('coupons.view_coupon',)
    model = Coupon
    paginate_by = 5
    template_name = 'pages/coupon-list.html'
    context_object_name = 'coupon_list'


class CouponCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('coupons.add_coupon',)
    model = Coupon
    form_class = CouponForm
    template_name = 'pages/create-coupon.html'
    success_url = reverse_lazy('coupons:coupon_list')


class CouponUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('coupons.change_coupon',)
    model = Coupon
    form_class = CouponForm
    template_name = 'pages/edit-coupon.html'
    success_url = reverse_lazy('coupons:coupon_list')


class CouponDeleteView(PermissionRequiredMixin, View):
    permission_required = ('coupons.delete_coupon',)

    def get(self, request, pk):
        coupon = Coupon.objects.get(pk=pk)
        coupon.delete()
        return redirect('coupons:coupon_list')
