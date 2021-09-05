from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView

from dealer.orders.models import Order


@login_required
def list_orders(request):
    orders = Order.objects.filter(
        car__dealer__user=request.user).prefetch_related('car__model')
    return render(
        request,
        'orders/list.html',
        {'orders': orders}
    )


class DetailOrderView(DetailView):
    model = Order
    pk_url_kwarg = 'order_pk'
    template_name = 'orders/detail.html'
    context_object_name = 'order'

# Create your views here.
