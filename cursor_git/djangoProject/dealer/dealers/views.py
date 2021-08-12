from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView

from dealer.dealers.models import Dealer
from dealer.cars.models import Car


def list_dealers_view(request):
    dealers = Dealer.objects.all()
    return render(
        request,
        'dealers/list.html',
        {'dealers': dealers}
    )


def detail_dealer_view(request, dealer_pk):
    dealer = Dealer.objects.filter(id=dealer_pk).first()
    cars = Car.objects.filter(dealer_id=dealer_pk)
    return render(
        request,
        'dealers/detail.html',
        {
            'dealer': dealer,
            'cars': cars,
        }
    )

# Create your views here.
