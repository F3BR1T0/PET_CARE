from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication

from account.api.serializers import AccountUpdateSerializer
from account.models import AppAccount 
from pet_owners.api import serializers
from pet_owners import models
from pet_owners.api.permissions import HasShareJunoApiKey
from pet_care_backend.utils import HttpResponseUtils as httputils

class PetOwnersViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.PetOwnersSerializers
    queryset = models.PetOwners.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    
    UserModel = AppAccount
    
    def get_queryset(self):
        if self.action in ("create","user_delete_petowner", "user_update_petowner", "get_petowner"):
            return models.PetOwners.objects.filter(email=self.request.user.email).first()
        return super().get_queryset()
    
    def get_serializer_class(self):
        if self.action == "create":
            return serializers.PetOwnerCreateSerializer
        if self.action == "find_by_email":
            return serializers.PetOwnersOnlyEmailSerializer
        if self.action == "user_update_petowner":
            return serializers.PetOwnerUpdateSerializer
        return super().get_serializer_class()
        
    def list(self, request):
        self.__check_if_is_admin(request)
        return super().list(request) 
    
    def retrieve(self, request, pk:None):
        self.__check_if_is_admin(request)
        return super().retrieve(request, pk)
    
    def update(self, request, pk:None):
        self.__check_if_is_admin(request)
        return super().update(request, pk)
    
    def partial_update(self, request):
        self.__check_if_is_admin(request)
        pass
    
    def destroy(self, request, pk: None):
        self.__check_if_is_admin(request)
        return super().destroy(request, pk)
        
    def create(self,request):    
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            try:
                user = self.get_queryset()
                
                if user:
                    return httputils.response('User already registered')
                
                if serializer.validated_data.get('email') != self.request.user.email:
                    return httputils.response_bad_request_400('Email is not the same as your account')
                
                serializer.save()
                
                return httputils.response_as_json(serializer.data, status.HTTP_201_CREATED)
            except Exception as e:
                httputils.response_bad_request_400(str(e))
        
        return httputils.response_as_json(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['put'], url_name='user update petowner', url_path='user-update-petowner')
    def user_update_petowner(self, request):
        serializer = self.get_serializer(data=request.data, instance=self.get_queryset())
        
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                
                request.data['username'] = request.user.username
                
                serializer_account = AccountUpdateSerializer(data=request.data, instance=request.user)
                if serializer_account.is_valid():
                    serializer_account.save()
                
                return httputils.response_as_json(serializer.data, status.HTTP_202_ACCEPTED)
            except Exception as e:
                return httputils.response_bad_request_400(str(e))
        return httputils.response_as_json(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'], url_name="get petowner", url_path='get-petowner')
    def get_petowner(self, request):
        try:
            userpetowner = self.get_queryset()
        
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
        
   
    @action(detail=False, methods=['post'], permission_classes=[HasShareJunoApiKey | IsAdminUser], url_path='findbyemail')
    def find_by_email(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            pet_owner = models.PetOwners.objects.filter(email=serializer.validated_data.get('email'))
            if pet_owner:
                response_serializer = serializers.PetOwnersSerializers(pet_owner)
                return httputils.response_as_json(response_serializer.data)
            return httputils.response('Pet owner not found', status.HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['delete'], permission_classes = [IsAuthenticated], authentication_classes=[SessionAuthentication])
    def user_delete_petowner(self, request):
        user = self.get_queryset()
        if user is None:
            return httputils.response_bad_request_400("Pet owner not found")    
        
        useraccount = self.UserModel.objects.get(email=user.email)
        if useraccount is None:
            return httputils.response_bad_request_400("Account not found")
        try:
            user.delete()
            useraccount.delete()
            logout(request)
            return httputils.response("User deleted successfuly")
        except Exception as e:
            return httputils.response_bad_request_400(str(e))
            
    def __check_if_is_admin(self,request):
        self.permission_classes = [IsAuthenticated, IsAdminUser]
        self.check_permissions(request)