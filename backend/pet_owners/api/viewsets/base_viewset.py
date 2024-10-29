from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import get_user_model

from pet_owners import models
from pet_care_backend.utils import HttpResponseUtils as http
from pet_care_backend.utils import ResponseMixin

class PetOwnerBaseViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    
    def get_queryset(self):
        return models.PetOwner.objects.filter(email = self.request.user.email).first()
    
    def _get_account(self):
        return get_user_model().objects.filter(email=self.request.user.email).first()