from django.shortcuts import render, redirect
from django.views.generic import FormView
from dealer.newemails import forms
from dealer.newemails.models import NewsLetter
from django.http import HttpResponse


def succes_view(request):
    return render(
        request,
        'newemails/succes.html'
    )


class NewLettersView(FormView):
    model = NewsLetter
    template_name = "newemails/subscribe.html"
    form_class = forms.NewLetterForm
    success_url = '/subscribe/succes'

    def form_valid(self, form):
        form.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        return HttpResponse('You are already subscribed')

# Create your views here.
