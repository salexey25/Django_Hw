from django.shortcuts import render
from .models import OrderModel
from django.utils import timezone
from django.utils.timezone import timedelta

# Create your views here.
def history_of_orders(request):
    client_id = 2
    orders_last_7_days = OrderModel.objects.filter(customer_id=client_id, date_order__gte=timezone.now() - timedelta(days=7))
    orders_last_30_days = OrderModel.objects.filter(customer_id=client_id, date_order__gte=timezone.now() - timedelta(days=30))
    orders_last_365_days = OrderModel.objects.filter(customer_id=client_id,date_order__gte=timezone.now() - timedelta(days=365))

    context = {
        'orders_last_7_days': orders_last_7_days,
        'orders_last_30_days': orders_last_30_days,
        'orders_last_365_days': orders_last_365_days,
    }

    return render(request, 'hw2app/history_of_orders.html', context)