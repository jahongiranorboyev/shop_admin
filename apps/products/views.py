# views.py
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView

from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Product
from apps.categories.models import Category
from apps.brands.models import Brand
from .forms import ProductForm


class ProductListView(PermissionRequiredMixin, ListView):
    permission_required = 'products.view_product'
    model = Product
    template_name = 'pages/products.html'
    paginate_by = 2


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'products.add_product'
    model = Product
    form_class = ProductForm
    template_name = 'pages/add-new-product.html'
    success_url = reverse_lazy('products:product-list')  # Redirect after successful creation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.filter(category__isnull=False)
        context['subcategories'] = Category.objects.filter(category__isnull=True)
        context['brands'] = Brand.objects.all()
        context['product'] = self.object or None
        return context

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        messages.success(self.request, "Product created successfully!")
        return redirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(self.get_context_data(form=form))


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'products.change_product'
    model = Product
    form_class = ProductForm
    template_name = 'pages/edit-product.html'
    success_url = reverse_lazy('products:product-list')

    def form_valid(self, form):
        messages.success(self.request, "Product updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(self.get_context_data(form=form))


class ProductDeleteView(PermissionRequiredMixin, View):
    permission_required = 'products.delete_product'

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        product.delete()
        messages.success(self.request, "Product deleted successfully!")
        return HttpResponseRedirect(reverse_lazy('products:product-list'))
