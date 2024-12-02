from django.urls import path

from apps.orders.views import OrderListView, DetailOrderView, OrderTrackingView

app_name = 'orders'
urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('detail/',DetailOrderView.as_view(), name='order_detail'),
    path('order-tracking',OrderTrackingView.as_view(), name='order_tracking'),
]