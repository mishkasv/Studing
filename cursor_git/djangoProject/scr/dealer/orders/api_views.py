from django.core.mail import send_mail
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from dealer.orders.models import Order
from dealer.orders.serializers import OrderSerializer


class OrderApiView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = []


    def perform_create(self, serializer):
        data = serializer.validated_data
        try:
            order=Order.objects.get(
                email=data.get('email'),
                phone=data.get('phone'),
                car = data.get('car')
            )
            if order:
               raise  ValidationError('You are already created order for this car')
        except Order.DoesNotExist:
            pass
        send_mail('Order for car', 'You order is created successfully','alish.floud@gmail.com',[data.get('email')])
        serializer.save()



