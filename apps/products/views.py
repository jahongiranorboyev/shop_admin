# views.py
from django.views.generic import ListView

from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Product
from apps.categories.models import Category
from apps.brands.models import Brand
from .forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'pages/products.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'pages/add-new-product.html'
    success_url = reverse_lazy('products:product-list')  # Redirect after successful creation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.filter(category__isnull=True)
        context['subcategories'] = Category.objects.filter(category__isnull=False)
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

