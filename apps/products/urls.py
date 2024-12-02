from django.urls import path

from apps.products.views import ProductListView, ProductCreateView
app_name ='products'
urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
]