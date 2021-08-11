from django.shortcuts import render
from dealer.orders.models import Order
from dealer.cars.models import Car


def list_orders(request):
    orders = Order.objects.filter(car)

# Create your views here.
