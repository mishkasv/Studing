from django.forms import ModelForm

from dealer.newemails.models import NewsLetter


class NewLetterForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'
