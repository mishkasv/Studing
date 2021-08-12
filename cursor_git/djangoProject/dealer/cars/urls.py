from django.urls import path, include
from dealer.cars import views

api_patterns = [
    path(
        'json',
        views.json_cars_view
    ),
    path(
        'json/<int:car_pk>',
        views.json_car_detail_view
    ),

]
urlpatterns = [
    path(
        '',
        views.list_cars_view,
    ),
    path(
        '<int:car_pk>/',
        views.DetailCarView.as_view(),
        name='detail'
    ),
    path(
        'api/',
        include(api_patterns),
        name='api'
    )
]
