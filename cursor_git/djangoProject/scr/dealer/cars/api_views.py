import datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from dealer.cars.helpful_function import add_view_to_car
from dealer.cars.permisions import CustomAuthentication
from dealer.cars.serializers import CarListSerializer, CarCreateUpdateSerializer, ColorSerializer, BrandSerializer, \
    ModelSerializer, FuelTypeSerializer
from dealer.cars.models import Car, Color, Brand, FuelType, Model_car
from rest_framework.pagination import PageNumberPagination


class ApiCarPublicListView(viewsets.ViewSet, PageNumberPagination):
    permission_classes = []
    authentication_classes = []

    def list(self, request):
        if request.GET.get('order_by'):
            order_by = request.GET.get('order_by')
            if order_by == 'model':
                order_by = 'model__name'
            elif order_by == 'brand':
                order_by = 'model__brand__name'
            elif order_by == 'dealer':
                order_by = 'dealer__id'
            queryset = Car.objects.filter(status_public=True).order_by(order_by)
        else:
            queryset = Car.objects.filter(status_public=True).order_by('id')
        page = self.paginate_queryset(queryset, request)
        if page is not None:
            serializer = CarListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = CarListSerializer(queryset, many=True)
        return Response(serializer.data, )

    def deateil(self, request, car_pk):
        queryset = Car.objects.filter(status_public=True)
        obj = get_object_or_404(queryset, pk=car_pk)
        obj.view_for_statistic = add_view_to_car(datetime.date.today(),obj.view_for_statistic)
        obj.save()
        serializer = CarListSerializer(obj)
        return Response(serializer.data)

class ApiCarPrivatListView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuthentication]


    def list(self, request):
        print(request.user, request.auth)
        queryset = Car.objects.filter(dealer__user=request.user)
        serializer = CarListSerializer(queryset, many=True)
        return Response(serializer.data, )

    def deateil(self, request, car_pk):
        queryset = Car.objects.filter(dealer__user=request.user)
        queryset = get_object_or_404(queryset, pk=car_pk)
        serializer = CarListSerializer(queryset)
        return Response(serializer.data)

class CRUDCarView(viewsets.ModelViewSet):
    serializer_class = CarCreateUpdateSerializer
    lookup_url_kwarg = "car_pk"
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuthentication]

    @action(detail=True, methods=['get'])
    def change_status_public(self, request, car_pk=None):
        queryset = self.get_object()
        queryset.status_public = True
        queryset.save()
        return Response({'status':'status public changed to public'})

    @action(detail=True, methods=['get'])
    def change_status_unpublic(self, request, car_pk=None):
        queryset = self.get_object()
        queryset.status_public = False
        queryset.save()
        return Response({'status':'status public changed to unpublic'})

    def get_queryset(self):
        return Car.objects.filter(dealer__user=self.request.user)

class CRUDColorView(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    lookup_url_kwarg = "color_pk"
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuthentication]
    def get_queryset(self):
        return Color.objects.filter(dealer__user=self.request.user)

class CRUDBrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_url_kwarg = "brand_pk"
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuthentication]
    def get_queryset(self):
        return Brand.objects.filter(dealer__user=self.request.user)

class CRUDModelView(viewsets.ModelViewSet):
    queryset = Model_car.objects.all()
    serializer_class = ModelSerializer
    lookup_url_kwarg = "model_pk"
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuthentication]
    def get_queryset(self):
        return Model_car.objects.filter(dealer__user=self.request.user)

class CRUDFuelTypeView(viewsets.ModelViewSet):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer
    lookup_url_kwarg = "fueltype_pk"
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuthentication]
    def get_queryset(self):
        return FuelType.objects.filter(dealer__user=self.request.user)


