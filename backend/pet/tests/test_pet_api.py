from rest_framework import status
from django.urls import reverse
from pet.models import Pet, HistoricoMedico
from .test_base import PetApiTestBase

class PetApiTestCase(PetApiTestBase):

    def test_register_and_get_pet(self):
        response = self.client.post(reverse('pets-register'), self.pet_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        pet = Pet.objects.first()
        self.assertIsNotNone(pet)
        self._verify_pet_data(response.data, self.pet_data)

        self.assertEqual(HistoricoMedico.objects.count(), 1)
        self.assertEqual(pet.pet_owner.email, self.owner.email)

        response = self.client.get(reverse('pets-get', args=[pet.pet_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self._verify_pet_data(response.data, self.pet_data)

    def test_update_pet(self):
        response = self.client.post(reverse('pets-register'), self.pet_data, format='json')
        pet = Pet.objects.first()

        update_data = {
            "nome": "Bobby UPDATED",
            "especie": "Cachorro",
            "raca": "Poodle",
            "peso": 15.0,
            "idade": 4,
            "sexo": "M",
        }
        response = self.client.put(reverse('pets-update', args=[pet.pet_id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        
        self._verify_pet_data(response.data, update_data)

    def test_delete_pet(self):
        response = self.client.post(reverse('pets-register'), self.pet_data, format='json')
        pet = Pet.objects.first()

        self.assertEqual(Pet.objects.count(), 1)
        response = self.client.delete(reverse('pets-delete', args=[pet.pet_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        self.assertEqual(Pet.objects.count(), 0)
        self.assertEqual(HistoricoMedico.objects.count(), 0)
