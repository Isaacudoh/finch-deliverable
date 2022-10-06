from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
User = get_user_model()



class SettingsBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        email = kwargs['username']
        password = kwargs['password']
        try:
            customer = User.objects.get(email=email)
            if customer.check_password(password) is True:
                return customer
        except User.DoesNotExist:
            pass
        
        