from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework import viewsets
from pet.api import serializers
from pet import models
from pet_owners.models import PetOwners
from pet_care_backend.utils import HttpResponseUtils as httputils
from pet_care_backend.utils import ResponseMixin

class PetBaseViewSet(viewsets.GenericViewSet):
    def _get_petowner(self):
        if self.request.user == 'AnonymusUser':
            raise Exception 
        petowner = PetOwners.objects.filter(email=self.request.user.email).first()
        if petowner is None:
            raise PetOwners.DoesNotExist
        return petowner
    
    def get_queryset(self):
        pet_owner = self._get_petowner()
        queryset = models.Pet.objects.filter(pet_owner = pet_owner)
        if queryset is None: 
                raise models.Pet.DoesNotExist
        return queryset

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

class PetMedicalHistoryViewSet(PetBaseViewSet):
    serializer_class = serializers.HistoricoMedicoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    
    def get_queryset(self, pk: None):
        pet_owner = self._get_petowner()
        medical_history = models.HistoricoMedico.objects.filter(pet__pet_owner=pet_owner, pet__pet_id = pk).first()
        if medical_history is None:
            raise models.HistoricoMedico.DoesNotExist
        
        return medical_history
    
    @action(detail=True, methods=['get'], url_name='get', url_path='get-by-pet')
    def get(self, request, pk:None):
        try:
            medical_history = self.get_queryset(pk)
            return httputils.response_as_json(serializers.HistoricoMedicoSerializer(medical_history).data)
        except Exception as e:
            return httputils.response_bad_request_400(str(e))
    
class PetMedicalHistoryVacinaViewSet(PetBaseViewSet, ResponseMixin):
    serializer_class = serializers.VacinaAdministradasSaveSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    
    def get_queryset(self):
        pet_owner = self._get_petowner()
        return models.VacinasAdministradas.objects.filter(historico_medico__pet__pet_owner = pet_owner)
    
    def get_serializer_class(self):
        action_serializers = {
            "update_vacina": serializers.VacinaAdministradasUpdateSerializer
        }
        return action_serializers.get(self.action, super().get_serializer_class())
        
    
    @action(detail=False, methods=['post'], url_name='add-vacina', url_path='add-vacina')
    def add_vacina(self, request):
        serializer = self.get_serializer(data=request.data)
        
        historico_medico_id = request.data.get('historico_medico')
                
        pet_owner = self._get_petowner()
        historico_medico = models.HistoricoMedico.objects.filter(pet__pet_owner=pet_owner, historico_medico_id = historico_medico_id).first()
        
        if not historico_medico:
                return httputils.response_bad_request_400("Medical history not found.")
            
        vacina_added = self.handle_serializer_errors(serializer)
        
        if vacina_added:
            return httputils.response_as_json(serializer.data, status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['delete'], url_name="delete-vacina", url_path="delete-vacina")
    def remove_vacina(self, request, pk: None):
        try:
            vacina_administrada = self.get_queryset().filter(vacinas_administradas_id = pk).first()
            
            if vacina_administrada is None:
                return httputils.response_bad_request_400("Vacina not found.")
            
            vacina_administrada.delete()
            return httputils.response("Vacina deleted.", status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return httputils.response_bad_request_400(str(e))
        
    @action(detail=True, methods=['put'], url_name='update-vacina')
    def update_vacina(self, request, pk: None):
        vacina_administrada = self.get_queryset().filter(vacinas_administradas_id = pk).first()
        if not vacina_administrada:
            return httputils.response('Vacina not found.', status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(instance=vacina_administrada, data = request.data)
        
        vacina_administrada_updated = self.handle_serializer_errors(serializer)
        
        if vacina_administrada_updated:
            return httputils.response_as_json(serializers.VacinasAdministradasSerializer(vacina_administrada_updated).data, status.HTTP_202_ACCEPTED)

class PetMedicalHistoriyVermifugoViewSet(PetBaseViewSet, ResponseMixin):
    serializer_class = serializers.VermifugosAdministradasSaveSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    
    def get_queryset(self):
        pet_owner = self._get_petowner()
        return models.VermifugosAdministrados.objects.filter(historico_medico__pet__pet_owner = pet_owner)
    
    @action(detail=False, methods=['post'], url_path='add-vermifugo')
    def add_vermifugo(self, request):
        serializer = self.get_serializer(data=request.data)
        
        historico_medico_id = request.data.get('historico_medico')
            
        pet_owner = self._get_petowner()
        historico_medico = models.HistoricoMedico.objects.filter(pet__pet_owner=pet_owner, historico_medico_id = historico_medico_id).first()
            
        if not historico_medico:
                return httputils.response_bad_request_400("Medical history not found.")
        
        vermifugo_added = self.handle_serializer_errors(serializer)
        
        if vermifugo_added:
            return httputils.response_as_json(serializer.data, status.HTTP_201_CREATED)