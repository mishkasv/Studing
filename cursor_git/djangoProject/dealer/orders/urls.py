from django.urls import path
from dealer.orders import views

urlpatterns = [
    path(
        '',
        views.list_orders, name='status'),
    path(
        '<order_pk>/',
        views.DetailOrderView.as_view(),
    ),
]
