from rest_framework import status
from django.urls import reverse
from pet.models import Pet, HistoricoMedico, Vacina, VacinaAdministrada
from .test_base import PetApiTestBase

class PetMedicalHistoryVacinaTestCase(PetApiTestBase):
    
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.vacina = Vacina.objects.create(nome="Vacina Exemplo")
        cls.vacina2 = Vacina.objects.create(nome="Vacina Exemplo Segundo")

    def test_add_vacina_administrada(self):
        response = self.client.post(reverse('pets-register'), self.pet_data, format='json')
        pet = Pet.objects.first()
        medical_history = HistoricoMedico.objects.filter(pet=pet).first()

        vacina_data = {
            "observacao": "Vacina administrada com sucesso",
            "data_aplicacao": "2024-10-21T02:43:37.669Z",
            "data_reforco": "2024-10-21T02:43:37.669Z",
            "vacina": f"{self.vacina.vacina_id}",
            "historico_medico": f"{medical_history.historico_medico_id}",
        }

        response = self.client.post(reverse('pets-medical-history-vacinas-add'), vacina_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        vacina_administrada = VacinaAdministrada.objects.first()
        self.assertEqual(vacina_administrada.vacina.nome, self.vacina.nome)

    def test_update_vacina_administrada(self):
        # Código para teste de atualização de vacina...
        pass

    def test_remove_vacina_administrada(self):
        # Código para teste de remoção de vacina...
        pass
