from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from .models import Coupon
from .forms import CouponForm


class CouponCreateView(CreateView):
    model = Coupon
    form_class = CouponForm
    template_name = 'pages/create-coupon.html'
    success_url = reverse_lazy('coupons:coupon_list')


class CouponUpdateView(UpdateView):
    model = Coupon
    form_class = CouponForm
    template_name = 'pages/edit-coupon.html'
    success_url = reverse_lazy('coupons:coupon_list')


class CouponDeleteView(View):
    def get(self, request, pk):
        coupon = Coupon.objects.get(pk=pk)
        coupon.delete()  # Delete the coupon
        return redirect('coupons:coupon_list')



class CouponListView(ListView):
    model = Coupon
    paginate_by = 5  # Define the number of coupons per page
    template_name = 'pages/coupon-list.html'

    # Optionally, you can override the context_object_name if you prefer a different variable name in the template
    context_object_name = 'coupon_list'
