
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.brands.forms import BrandForm
from apps.brands.models import Brand


class BrandListView(ListView):
    model = Brand
    template_name = 'pages/brand_list.html'
    context_object_name = 'brands'
class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'pages/brand_form.html'
    success_url = reverse_lazy('brands:brand_list')  # Redirect after successful form submission

class BrandUpdateView(UpdateView):
    model = Brand
    template_name = 'pages/brand_edit.html'
    fields = ['name',]
    success_url = reverse_lazy('brands:brand_list')

class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'pages/brand_confirm_delete.html'
    success_url = reverse_lazy('brands:brand_list')