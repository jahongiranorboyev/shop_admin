from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Category
from .forms import CategoryForm


class CategoryListView(ListView):
    model = Category
    template_name = 'pages/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'pages/category_form.html'
    success_url = reverse_lazy('categories:category_list')  # Redirect after successful form submission


# Category Update View
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'pages/category_edit.html'
    success_url = reverse_lazy('categories:category_list')

    def form_valid(self, form):
        messages.success(self.request, "Category updated successfully!")
        return super().form_valid(form)


# Category Delete View
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'pages/category_delete_confirm.html'
    success_url = reverse_lazy('categories:category_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Category deleted successfully!")
        return super().delete(request, *args, **kwargs)