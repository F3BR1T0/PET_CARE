from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication

from pet_owners.api import serializers
from pet_owners import models
from pet_owners.api.permissions import HasShareJunoApiKey
from pet_care_backend.utils import HttpResponseUtils as httputils

class PetOwnersViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.PetOwnersSerializers
    queryset = models.PetOwners.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    
    def get_queryset(self):
        if self.action == "create":
            return models.PetOwners.objects.filter(email=self.request.user.email)
        return super().get_queryset()
    
    def get_serializer_class(self):
        if self.action == "create":
            return serializers.PetOwnerCreateSerializer
        return super().get_serializer_class()
    
    def list(self, request):
        self.permission_classes = [IsAuthenticated, IsAdminUser]
        self.check_permissions(request)
        return 
    
    def create(self,request):    
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            try:
                user = self.get_queryset().first()
                
                if user:
                    return httputils.response('User already registered')
                
                if serializer.validated_data.get('email') != self.request.user.email:
                    return httputils.response_bad_request_400('Email is not the same as your account')
                
                serializer.save()
                return httputils.response_as_json(serializer.data, status.HTTP_201_CREATED)
            except Exception as e:
                httputils.response_bad_request_400(str(e))
        
        return httputils.response_as_json(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'], url_name="get petowner", url_path='get-petowner')
    def get_petowner(self, request):
        try:
            userpetowner = self.get_queryset().first()
            
            if userpetowner:
                return httputils.response_as_json({
                    'username-login': request.user.username,
                    'name': userpetowner.name,
                    'email': userpetowner.email,
                    'photo': userpetowner.foto,
                    'cpf': userpetowner.cpf,
                    'telefone': userpetowner.telefone,
                    'created_at': userpetowner.create_at,
                    'updated_at': userpetowner.update_at
                })
            return httputils.response_bad_request_400('User is not registered')
        except Exception as e:
            return httputils.response_bad_request_400(str(e))
    
    def get_serializer_class(self):
        if self.action == "find_by_email":
            return serializers.PetOwnersOnlyEmailSerializers
        return super().get_serializer_class()
        
    @action(detail=False, methods=['post'], permission_classes=[HasShareJunoApiKey], url_path='findbyemail')
    def find_by_email(self, request):
        email = request.data['email']
        pet_owner = models.PetOwners.objects.filter(email=email).first()
        if pet_owner:
            response_serializer = serializers.PetOwnersSerializers(pet_owner)
            return httputils.response_as_json(response_serializer.data)
        return httputils.response('Pet owner not found', status.HTTP_404_NOT_FOUND)
    
    
    
 
    