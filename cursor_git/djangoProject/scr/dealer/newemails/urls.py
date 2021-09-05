from django.urls import path
from dealer.newemails import views

urlpatterns = [
    path(
        '',
        views.NewLettersView.as_view()
    ),
    path(
        'succes',
        views.succes_view
    )
]
