from django.urls import path
from dealer.users import views

app_name = 'users'
urlpatterns = [
    path(
        'login/',
        views.LoginView.as_view(),
        name='login-page'
    ),
    path(
        'logout',
        views.LogoutView.as_view()
    )
]
