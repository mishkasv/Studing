from scr.dealer.orders.models import Order


def list_orders(request):
    orders = Order.objects.filter(car)

# Create your views here.
