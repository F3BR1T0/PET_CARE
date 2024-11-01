from rest_framework import viewsets, status, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from pet_care_backend.utils import HttpResponseUtils as http
from ...models import PetOwner

class PetBaseViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    
    def _get_petowner(self):
        return PetOwner.objects.filter(email=self.request.user.email).first()
