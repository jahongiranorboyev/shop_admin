from django.urls import path

from apps.brands.views import BrandListView, BrandCreateView, BrandUpdateView, BrandDeleteView

app_name = 'brands'
urlpatterns = [
    path('', BrandListView.as_view(), name='brand_list'),
    path('brand/create/', BrandCreateView.as_view(), name='brand_create'),
    path('update/<uuid:pk>/', BrandUpdateView.as_view(), name='brand_update'),
    path('delete/<uuid:pk>/', BrandDeleteView.as_view(), name='brand_delete'),
]
