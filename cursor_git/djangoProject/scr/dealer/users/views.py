from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from dealer.users.forms import LoginForm


class LoginView(View):
    form = LoginForm

    def get(self, request):
        if not request.user.is_anonymous:
            return HttpResponseRedirect('/')
        return self._login_page(request, context={})

    def _login_page(self, request, context=None):
        context = context or {}
        context['login_form'] = self.form()

        return render(request=request, template_name='users/login_form.html', context=context)

    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():
            login(request, form.cleaned_data['user'])
            return HttpResponseRedirect('/')

        return self._login_page(request, {"errors": form.errors})


class LogoutView(View):
    def get(self, request):
        if request.user.is_anonymous:
            return HttpResponseRedirect('/')
        return self._logout(request)

    def _logout(self, request):
        request.user.auth_token.is_active=False
        logout(request)

        return HttpResponseRedirect('/')
