from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView
from dealer.cars.models import Car
from rest_framework.authtoken.models import Token


@login_required(login_url='/users/login')
def list_cars_view(request):
    token, created = Token.objects.get_or_create(user=request.user)
    if token:
        cars = Car.objects.filter(
            dealer__user=request.user).prefetch_related(
            'model').prefetch_related('dealer__user')
        return render(
            request,
            'cars/list.html',
            {'cars': cars}
        )


class DetailCarView(DetailView):
    pk_url_kwarg = 'car_pk'
    template_name = 'cars/detail.html'
    context_object_name = 'car'

    def get_queryset(self):
        return Car.objects.all().prefetch_related('picture').prefetch_related('dealer__user')

# Create your views here.
