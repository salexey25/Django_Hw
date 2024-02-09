from django.urls import path
from .views import history_of_orders

urlpatterns = [
    path('history_of_orders/', history_of_orders, name='history_of_orders'),
]