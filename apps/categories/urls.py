from django.urls import path
from .views import CategoryListView,CategoryCreateView, CategoryUpdateView, CategoryDeleteView
app_name ='categories'
urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('<uuid:pk>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('<uuid:pk>/delete/',CategoryDeleteView.as_view(), name='category_delete'),

]
