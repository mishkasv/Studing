from django.http import HttpResponse
from django.shortcuts import render, redirect
import os
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from dealer.cars.models import Car, Picture


def redirect_page(request):
    return redirect('/1')


def status(request):
    return HttpResponse("OK")


def index_view(request):
    pictures = Picture.objects.all()
    page = request.GET.get('page', 1)
    cars = Car.objects.all()
    paginator = Paginator(cars, 5)
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    return render(
        request,
        os.path.join(r'C:\Users\Gazik\studing\cursor_git\djangoProject\templates\index.html'),
        {
            'cars': cars,
            'pictures': pictures,
        }
    )
