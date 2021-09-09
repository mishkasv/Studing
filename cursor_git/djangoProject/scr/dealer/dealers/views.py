from django.shortcuts import render

from dealer.dealers.models import Dealer


def list_dealers_view(request):
    dealers = Dealer.objects.all().prefetch_related('user')
    return render(
        request,
        'dealers/list.html',
        {'dealers': dealers}
    )


def detail_dealer_view(request, dealer_pk):
    dealer = Dealer.objects.filter(id=dealer_pk).prefetch_related('dealers_cars__model').first()
    return render(
        request,
        'dealers/detail.html',
        {'dealer': dealer, }
    )

# Create your views here.
