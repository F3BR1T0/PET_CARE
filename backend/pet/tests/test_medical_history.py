from rest_framework import status
from django.urls import reverse
from pet.models import Pet, HistoricoMedico
from .test_base import PetApiTestBase

class PetMedicalHistoryTestCase(PetApiTestBase):

    def test_get_medical_history(self):
        response = self.client.post(reverse('pets-register'), self.pet_data, format='json')
        pet = Pet.objects.first()

        response = self.client.get(reverse('pets-medical-history-get', args=[pet.pet_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['pet']['nome'], pet.nome)
