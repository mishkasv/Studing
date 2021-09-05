from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication
from django.utils.translation import gettext_lazy as _

class CustomAuthentication(TokenAuthentication):
    def get_model(self):
        if self.model is not None:
            return self.model
        from scr.dealer.users.models import CustomToken
        return CustomToken


    def authenticate_credentials(self, key):

        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))
        if not token.is_active:
            raise exceptions.AuthenticationFailed(_('User is logged out.'))
        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (token.user, token)