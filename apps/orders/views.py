from django.views.generic import ListView, DetailView

from apps.orders.models import Order


class OrderListView(ListView):
    model = Order
    template_name = 'pages/order-list.html'

class DetailOrderView(DetailView):
    model = Order
    template_name = 'pages/order-detail.html'


class OrderTrackingView(DetailView):
    model = Order
    template_name = 'pages/order-tracking.html'
