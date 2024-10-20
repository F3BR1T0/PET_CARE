from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework import viewsets
from pet.api import serializers
from pet import models
from pet_owners.models import PetOwners
from pet_care_backend.utils import HttpResponseUtils as httputils

class PetBaseViewSet(viewsets.GenericViewSet):
    def _get_petowner(self):
        petowner = PetOwners.objects.filter(email=self.request.user.email).first()
        if petowner is None:
            raise PetOwners.DoesNotExist
        return petowner

class PetViewSet(PetBaseViewSet):
    serializer_class = serializers.PetSaveSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    
    def get_queryset(self):
        pet_owner = self._get_petowner()
        queryset = models.Pet.objects.filter(pet_owner = pet_owner)
        if queryset is None: 
             raise models.Pet.DoesNotExist
        return queryset
    
    @action(detail=False, methods=['post'], url_name='register', url_path='register')
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            try:
                pet_owner = self._get_petowner()
                if pet_owner is None:
                    raise PetOwners.DoesNotExist
                pet = serializer.save(pet_owner = pet_owner)
                models.HistoricoMedico.objects.create(pet = pet)
                
                return httputils.response_as_json(serializers.PetSerializer(pet).data, status.HTTP_201_CREATED)
            except PetOwners.DoesNotExist:
                return httputils.response_bad_request_400("Pet Owner does not exists.")
            except Exception as e:
                return httputils.response_bad_request_400(str(e))
        return httputils.response_as_json(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'], url_name='get', url_path='get')
    def get(self, request, pk:None):
        try:
            pet = self.get_queryset().filter(pet_id = pk).first()
            return httputils.response_as_json(serializers.PetSerializer(pet).data)
        except PetOwners.DoesNotExist:
            return httputils.response_bad_request_400("Pet Owner does not exists.")
        except models.Pet.DoesNotExist:
            return httputils.response_bad_request_400("Pet does not exists.")
        except Exception as e:
                return httputils.response_bad_request_400(str(e))
    

    @action(detail=True, methods=['put'], url_name='update', url_path='update')
    def update_pet(self, request, pk:None):
        serializer = self.get_serializer(data=request.data, instance=self.get_queryset().filter(pet_id = pk).first())
        
        if serializer.is_valid(raise_exception=True):
            try:
                pet = serializer.save()
                return httputils.response_as_json(serializers.PetSerializer(pet).data, status.HTTP_202_ACCEPTED)
            except Exception as e:
                return httputils.response_bad_request_400(str(e))
        return httputils.response_as_json(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['delete'], url_name='delete', url_path='delete')
    def delete(self, request, pk:None):
        try:
            pet = self.get_queryset().filter(pet_id = pk).first()
            pet.delete()
            return httputils.response("Pet deleted", status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return httputils.response_bad_request_400(str(e))
                
    