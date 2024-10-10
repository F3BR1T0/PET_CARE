from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from address.api.serializers import AddressSerializer
from account.models import AppAccount 
from pet_owners.api import serializers
from pet_owners import models
from pet_owners.api.permissions import HasShareJunoApiKey
from pet_care_backend.utils import HttpResponseUtils as httputils

class PetOwnersViewSetBase(viewsets.GenericViewSet):
    UserModel = AppAccount
    
    def _get_account(self):
        return self.UserModel.objects.filter(email=self.request.user.email).first()

class PetOwnersViewSet(PetOwnersViewSetBase):
    serializer_class = serializers.PetOwnerSaveSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    
    def get_queryset(self):
        return models.PetOwners.objects.filter(email=self.request.user.email).first()
    
    @action(detail=False, methods=['post'], url_path='register', url_name='register')
    def register(self,request):    
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            try:
                user = self.get_queryset()
                
                if user:
                    return httputils.response('User already registered')
                
                if serializer.validated_data.get('email') != self.request.user.email:
                    return httputils.response_bad_request_400('Email is not the same as your account')
                
                response = serializer.save()
                
                serializer_response = serializers.PetOwnerSaveSerializer(response)
                
                return httputils.response_as_json(serializer_response.data, status.HTTP_201_CREATED)
            except Exception as e:
                httputils.response_bad_request_400(str(e))
        
        return httputils.response_as_json(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['put'], url_name='update petowner', url_path='update-petowner')
    def update_petowner(self, request):
        serializer = self.get_serializer(data=request.data, instance=self.get_queryset())
        account = self._get_account()
        
        
        if serializer.is_valid(raise_exception=True):
            try:
                response = serializer.save()
                account.email = serializer.validated_data['email']
                account.save()
                serializer_response = serializers.PetOwnersSerializer(response)
                return httputils.response_as_json(serializer_response.data, status.HTTP_202_ACCEPTED)
            except Exception as e:
                return httputils.response_bad_request_400(str(e))
        return httputils.response_as_json(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'], url_name="get petowner", url_path='get-petowner')
    def get_petowner(self, request):
        try:
            userpetowner = self.get_queryset()
            if userpetowner is None:
                return httputils.response_bad_request_400('Not registered')
            address_data = userpetowner.address
            if address_data is not None:
                address_data = AddressSerializer(userpetowner.address).data
            if userpetowner:
                return httputils.response_as_json({
                    'username-login': request.user.username,
                    'name': userpetowner.name,
                    'email': userpetowner.email,
                    'photo': userpetowner.foto,
                    'cpf': userpetowner.cpf,
                    'address': address_data,
                    'telefone': userpetowner.telefone,
                    'created_at': userpetowner.create_at,
                    'updated_at': userpetowner.update_at
                })
            return httputils.response_bad_request_400('User is not registered')
        except Exception as e:
            return httputils.response_bad_request_400(str(e))
           
    @action(detail=False, methods=['delete'], url_name='delete petowner', url_path='delete-petowner')
    def delete_petowner(self, request):
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
        
class PetOwnerAddressViewSet(PetOwnersViewSetBase):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    
    def get_queryset(self):
        return models.PetOwners.objects.filter(email = self.request.user.email).first()
    
    @action(detail=False, methods=['post'], url_name="create address", url_path="create")
    def register_address(self, request):
        serializer = self.serializer_class(data=request.data)
        petowner = self.get_queryset()
        
        if petowner.address is not None:
            return httputils.response_bad_request_400("Already have a address.")
        
        
        if serializer.is_valid(raise_exception=True):
            try:
                address_created = serializer.save()
                if address_created is not None:
                    petowner.address = address_created
                    petowner.save()
                return httputils.response_as_json(serializer.data)
                pass
            except Exception as e:
                return httputils.response_bad_request_400(str(e))
        
        return httputils.response_as_json(serializer.errors, status.HTTP_400_BAD_REQUEST)
   
    @action(detail=False, methods=['put'], url_name="update address", url_path="update")
    def update_address(self, request):
        petowner = self.get_queryset()
        if petowner.address is None:
            return httputils.response_bad_request_400("Petowner does not have a address.")
        
        serializer = self.serializer_class(data=request.data, instance=petowner.address)
        
        if serializer.is_valid():
            try:
                serializer.save()
                return httputils.response_as_json(serializer.data, status.HTTP_202_ACCEPTED)
            except Exception as e:
                return httputils.response_bad_request_400(str(e))
        return httputils.response_as_json(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
class PetOwnersAdminViewSet(viewsets.ModelViewSet, PetOwnersViewSetBase):
    
    serializer_class = serializers.PetOwnersSerializer
    queryset = models.PetOwners.objects.all()
    permission_classes = [IsAuthenticated & IsAdminUser]
    authentication_classes = [SessionAuthentication]
        

    def create(self, request):
        return httputils.response_bad_request_400("Not implemented")
    def list(self, request):
        return super().list(request) 
    
    def retrieve(self, request, pk:None):
        return super().retrieve(request, pk)
    
    def update(self, request, pk:None):
        return super().update(request, pk)
    
    def partial_update(self, request):
        return httputils.response_bad_request_400("Not implemented")
    
    def destroy(self, request, pk: None):
        return super().destroy(request, pk)
    
class PetOwnersExtraViewSet(viewsets.GenericViewSet):
    serializer_class = serializers.PetOwnersOnlyEmailSerializer
    permission_classes = [HasShareJunoApiKey]
    
    @action(detail=False, methods=['post'], url_name='findbyemail', url_path='findbyemail')
    def find_by_email(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            petowner = models.PetOwners.objects.filter(email=serializer.data.get('email')).first()
            if petowner is None:
                return httputils.response_bad_request_400("Not found.")
            return httputils.response_as_json(petowner)
        return httputils.response_as_json(serializer.errors, status.HTTP_400_BAD_REQUEST)
            