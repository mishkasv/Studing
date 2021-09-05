from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from dealer.cars.models import Car

def redirect_page(request):
    return redirect('/1')


def status(request):
    return HttpResponse("OK")


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def index_view(request):
    page = request.GET.get('page', 1)
    cars = Car.objects.order_by('id').prefetch_related('picture').prefetch_related('model')
    paginator = Paginator(cars, 5)
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    return render(
        request,
        'index.html',
        {'cars': cars,},

    )
