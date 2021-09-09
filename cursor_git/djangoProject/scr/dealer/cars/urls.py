from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from dealer.cars import api_views, views

app_name = 'cars'

api_privat_patterns = [
    path(
        'token-auth/',
        obtain_auth_token
    ),
    path(
        'colors/',
        api_views.CRUDColorView.as_view({'post': 'create', 'get': 'list'})
    ),
    path(
          'color/<int:color_pk>',
          api_views.CRUDColorView.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})
    ),
    path(
        'cars/',
        api_views.CRUDCarView.as_view({'post': 'create', 'get': 'list'})
    ),
    path(
        'car/<int:car_pk>',
        api_views.CRUDCarView.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})
    ),
    path(
        'car/<int:car_pk>/status_public',
        api_views.CRUDCarView.as_view({'get': 'change_status_public'})
    ),
    path(
        'car/<int:car_pk>/change_status',
        api_views.CRUDCarView.as_view({'get': 'change_status_uppublic'})
    ),
    path(
        'brands/',
        api_views.CRUDBrandView.as_view({'post': 'create', 'get': 'list'})
    ),
    path(
        'brand/<int:brand_pk>',
        api_views.CRUDBrandView.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})
    ),
    path(
        'models/',
        api_views.CRUDModelView.as_view({'post': 'create', 'get': 'list'})
    ),
    path(
        'model/<int:model_pk>',
        api_views.CRUDModelView.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})
    ),
    path(
        'fueltypes/',
        api_views.CRUDColorView.as_view({'post': 'create', 'get': 'list'})
    ),
    path(
        'fueltype/<int:fueltype_pk>',
        api_views.CRUDColorView.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})
    ),

]
api_public_patterns = [
    path(
        'cars/',
        api_views.ApiCarPublicListView.as_view({'get': 'list'})
    ),
    path(
        'car/<int:car_pk>',
        api_views.ApiCarPublicListView.as_view({'get': 'deateil'})
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
]
