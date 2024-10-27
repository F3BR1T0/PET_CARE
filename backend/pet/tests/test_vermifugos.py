from rest_framework import status
from django.urls import reverse
from pet.models import Pet, HistoricoMedico, VermifugoAdministrado, Vermifugo
from .test_base import PetApiTestBase

class PetMedicalHistoriyVermifugoTestCase(PetApiTestBase):
    
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.vermifugo = Vermifugo.objects.create(nome="Vermifugo Exemplo")
        cls.vermifugo2 = Vermifugo.objects.create(nome="Vermifugo Exemplo Segundo")
    
    def test_add_vermifugo(self):
        self.client.post(reverse('pets-register'), self.pet_data, format='json')
        pet = Pet.objects.first()
        medical_history = HistoricoMedico.objects.filter(pet=pet).first()

        vermifugo_data = {
            "observacao": "Vermífugo administrado com sucesso",
            "data_aplicacao": "2024-10-21T02:43:37.669Z",
            "vermifugo": f"{self.vermifugo.vermifugo_id}",
            "historico_medico": f"{medical_history.historico_medico_id}",
        }

        response = self.client.post(reverse('pets-medical-history-vermifugos-add'), vermifugo_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        vermifugo_administrado = VermifugoAdministrado.objects.first()
        self.assertEqual(vermifugo_administrado.historico_medico.historico_medico_id, medical_history.historico_medico_id)
    
    def test_update_vermifugo(self):
        self.client.post(reverse('pets-register'), self.pet_data, format='json')
        pet = Pet.objects.first()
        medical_history = HistoricoMedico.objects.filter(pet=pet).first()

        vermifugo_data = {
            "observacao": "Vermífugo administrado com sucesso",
            "data_aplicacao": "2024-10-21T02:43:37.669Z",
            "vermifugo": f"{self.vermifugo.vermifugo_id}",
            "historico_medico": f"{medical_history.historico_medico_id}",
        }

        self.client.post(reverse('pets-medical-history-vermifugos-add'), vermifugo_data, format="json")
        
        vermifugo_added = VermifugoAdministrado.objects.first()
        
        vermifugo_data = {
            "observacao": "Vermífugo administrado com sucesso UPDATED",
            "data_aplicacao": "2024-10-21T02:43:37.669Z",
            "vermifugo": f"{self.vermifugo2.vermifugo_id}",
            "historico_medico": f"{medical_history.historico_medico_id}",
        }
        
        response = self.client.put(reverse('pets-medical-history-vermifugos-update', args=[vermifugo_added.vermifugo_administrado_id]), vermifugo_data, format='json')
        
        vermifugo_added.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data['vermifugo']['nome'], self.vermifugo2.nome)
        self.assertEqual(response.data['observacao'], vermifugo_added.observacao)
        
    def test_delete_vermifugo(self):
        self.client.post(reverse('pets-register'), self.pet_data, format='json')
        pet = Pet.objects.first()
        medical_history = HistoricoMedico.objects.filter(pet=pet).first()

        vermifugo_data = {
            "observacao": "Vermífugo administrado com sucesso",
            "data_aplicacao": "2024-10-21T02:43:37.669Z",
            "vermifugo": f"{self.vermifugo.vermifugo_id}",
            "historico_medico": f"{medical_history.historico_medico_id}",
        }

        self.client.post(reverse('pets-medical-history-vermifugos-add'), vermifugo_data, format="json")
        
        vermifugo_added = VermifugoAdministrado.objects.first()
    
        self.client.delete(reverse('pets-medical-history-vermifugos-delete', args=[vermifugo_added.vermifugo_administrado_id]), format='json')
        
        self.assertEqual(VermifugoAdministrado.objects.count(), 0)