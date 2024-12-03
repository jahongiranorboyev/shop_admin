from django.urls import path

from apps.products.views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name ='products'
urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<uuid:pk>/edit/', ProductUpdateView.as_view(), name='product-edit'),
    path('<uuid:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]