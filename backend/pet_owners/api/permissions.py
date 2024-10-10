from rest_framework_api_key.permissions import BaseHasAPIKey
from rest_framework_api_key.models import APIKey
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from decouple import config

class HasShareJunoApiKey(BaseHasAPIKey):
    model = APIKey
    def has_permission(self, request, view):
        api_key = self.get_key(request)
                
        if not api_key:
            return False
        
        if super().has_permission(request,view) and api_key == config('JUNO_SECRET_KEY'):
            return request.method in ['POST']
        
        return False
        