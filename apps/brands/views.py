from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.brands.forms import BrandForm
from apps.brands.models import Brand


class BrandListView(PermissionRequiredMixin, ListView):
    permission_required = 'brands.view_brand'
    model = Brand
    template_name = 'pages/brand_list.html'
    context_object_name = 'brands'


class BrandCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'brands.add_brand'
    model = Brand
    form_class = BrandForm
    template_name = 'pages/brand_form.html'
    success_url = reverse_lazy('brands:brand_list')  # Redirect after successful form submission


class BrandUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'brands.edit_brand'
    model = Brand
    template_name = 'pages/brand_edit.html'
    fields = ['name', ]
    success_url = reverse_lazy('brands:brand_list')


class BrandDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'brands.delete_brand'
    model = Brand
    template_name = 'pages/brand_confirm_delete.html'
    success_url = reverse_lazy('brands:brand_list')
