from django.urls import path
from dealer.dealers import views

urlpatterns = [
    path(
        '',
        views.list_dealers_view,
    ),
    path(
        '<dealer_pk>/',
        views.detail_dealer_view,
    ),
]
