from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Category
from .forms import CategoryForm


class CategoryListView(PermissionRequiredMixin, ListView):
    permission_required = 'categories.view_category'
    model = Category
    template_name = 'pages/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'categories.add_category'
    model = Category
    form_class = CategoryForm
    template_name = 'pages/category_form.html'
    success_url = reverse_lazy('categories:category_list')  # Redirect after successful form submission


# Category Update View
class CategoryUpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = 'categories.change_category'
    model = Category
    form_class = CategoryForm
    template_name = 'pages/category_edit.html'
    success_url = reverse_lazy('categories:category_list')

    def form_valid(self, form):
        messages.success(self.request, "Category updated successfully!")
        return super().form_valid(form)


# Category Delete View
class CategoryDeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = 'categories.delete_category'
    model = Category
    template_name = 'pages/category_delete_confirm.html'
    success_url = reverse_lazy('categories:category_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Category deleted successfully!")
        return super().delete(request, *args, **kwargs)
