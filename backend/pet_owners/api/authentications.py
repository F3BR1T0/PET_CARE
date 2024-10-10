from rest_framework.authentication import BaseAuthentication

class CustomJunoAuthentication(BaseAuthentication):
    def authenticate(self, request):
        pass