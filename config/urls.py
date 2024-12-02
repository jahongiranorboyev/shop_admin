"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.authentications.views import CustomLoginView
from apps.general.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home-page'),
    path('auth/',include('apps.authentications.urls', namespace='authentications')),
    path('social/', include('social_django.urls')),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),


    #========== USERS URLS ==========
    path('users/',include('apps.users.urls',namespace='users')),

    #========== ORDERS URLS ==========
    path('orders/',include('apps.orders.urls',namespace='orders')),

    #   ========== PRODUCT URLS ==========
    path('products/',include('apps.products.urls',namespace='products')),

    #   ========== COUPONS URLS ==========
    path('coupons/',include('apps.coupons.urls',namespace='coupons')),

    #   ========== TICKETS URLS ==========
    path('tickets/', include('apps.tickets.urls', namespace='tickets')),

    #   ========== REPORTS URLS ==========
    path('reports/', include('apps.reports.urls', namespace='reports')),

    #========== CATEGORIES URLS ==========
    path('categories/',include('apps.categories.urls',namespace='categories')),

    #========== CATEGORIES URLS ==========
    path('brands/',include('apps.brands.urls',namespace='brands')),

    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

]