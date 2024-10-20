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
        return PetOwners.objects.filter(email=self.request.user.email).first()

class PetViewSet(PetBaseViewSet):
    serializer_class = serializers.PetSaveSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    
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
            pet_owner = self._get_petowner()
            
            if pet_owner is None:
                raise PetOwners.DoesNotExist
            
            pet = models.Pet.objects.filter(pet_owner = pet_owner).filter(pet_id = pk).first()
            if pet is None:
                raise models.Pet.DoesNotExist
            
            return httputils.response_as_json(serializers.PetSerializer(pet).data)
        except PetOwners.DoesNotExist:
            return httputils.response_bad_request_400("Pet Owner does not exists.")
        except models.Pet.DoesNotExist:
            return httputils.response_bad_request_400("Pet does not exists.")
        except Exception as e:
                return httputils.response_bad_request_400(str(e))
            
    