from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView
from django.core import serializers
from dealer.cars.models import Car, Picture
from django.http import HttpResponse


@login_required
def list_cars_view(request):
    cars = Car.objects.filter(dealer__user=request.user)
    return render(
        request,
        'cars/list.html',
        {'cars': cars}
    )


class DetailCarView(DetailView):
    model = Car
    pk_url_kwarg = 'car_pk'
    template_name = 'cars/detail.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super(DetailCarView, self).get_context_data(**kwargs)
        context.update({
            'picture': Picture.objects.filter(car_id=self.get_object().id).first(),
        })
        return context


def json_cars_view(request):
    data = serializers.serialize('json', Car.objects.all())
    return HttpResponse(data)


def json_car_detail_view(request, car_pk):
    data = serializers.serialize('json', [Car.objects.get(id=car_pk)])
    return HttpResponse(data)
# Create your views here.
