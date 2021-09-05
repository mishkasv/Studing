from django.urls import path
from dealer.dealers import api_views, views

app_name = 'dealers'

urlpatterns = [
    path(
        '',
        views.list_dealers_view,
    ),
    path(
        'statistics/',
        api_views.StatisticAllView.as_view(),
    ),
    path(
        'statistic/<int:car_pk>',
        api_views.StatisticByCarView.as_view(),
    ),
    path(
        '<dealer_pk>/',
        views.detail_dealer_view,
    ),
]

