from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from pet.models import Pet, HistoricoMedico, Vacinas, VacinasAdministradas
from pet_owners.models import PetOwners
from account.models import AppAccount

class PetApiTestBase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        default_email = "user@example.com"
        
        # Criar conta de usuário
        cls.account = AppAccount.objects.create(email=default_email, username="user")
        cls.account.set_password('password')
        cls.account.save()

        # Criar o dono do pet
        cls.owner = PetOwners.objects.create(nome='User', email=default_email)
        
        # Dados do pet
        cls.pet_data = {
            "nome": "Bobby",
            "especie": "Cachorro",
            "raca": "Poodle",
            "peso": 12.5,
            "idade": 3,
            "sexo": "M",
            "pet_owner": cls.owner.id_pet_owners
        }
    
    def setUp(self):
        # Autenticar o usuário para cada teste
        self.client.force_authenticate(self.account)
    
    def _verify_pet_data(self, response_data, expected_data):
        """Função auxiliar para verificar os dados do pet."""
        self.assertEqual(response_data['nome'], expected_data['nome'])
        self.assertEqual(response_data['especie'], expected_data['especie'])
        self.assertEqual(response_data['raca'], expected_data['raca'])
        self.assertEqual(float(response_data['peso']), float(expected_data['peso']))
        self.assertEqual(response_data['idade'], expected_data['idade'])
        self.assertEqual(response_data['sexo'], expected_data['sexo'])

class PetApiTestCase(PetApiTestBase):

    def test_register_and_get_pet(self):
        # Registrar o pet
        response = self.client.post(reverse('pets-register'), self.pet_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificar se o pet foi criado
        pet = Pet.objects.first()
        self.assertIsNotNone(pet)
        self._verify_pet_data(response.data, self.pet_data)

        # Verificar histórico médico
        self.assertEqual(HistoricoMedico.objects.count(), 1)
        self.assertEqual(pet.pet_owner.email, self.owner.email)

        # Testar GET para obter o pet
        response = self.client.get(reverse('pets-get', args=[pet.pet_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self._verify_pet_data(response.data, self.pet_data)

    def test_update_pet(self):
        # Registrar o pet
        response = self.client.post(reverse('pets-register'), self.pet_data, format='json')
        pet = Pet.objects.first()

        # Atualizar o pet
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
        
        # Verificar os dados atualizados
        self._verify_pet_data(response.data, update_data)

    def test_delete_pet(self):
        # Registrar o pet
        response = self.client.post(reverse('pets-register'), self.pet_data, format='json')
        pet = Pet.objects.first()

        # Verificar que o pet foi criado
        self.assertEqual(Pet.objects.count(), 1)

        # Deletar o pet
        response = self.client.delete(reverse('pets-delete', args=[pet.pet_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verificar se o pet e o histórico médico foram excluídos
        self.assertEqual(Pet.objects.count(), 0)
        self.assertEqual(HistoricoMedico.objects.count(), 0)

class PetMedicalHistoryTestCase(PetApiTestBase):

    def test_get_medical_history(self):
        # Registrar o pet
        response = self.client.post(reverse('pets-register'), self.pet_data, format='json')
        pet = Pet.objects.first()

        # Obter histórico médico
        response = self.client.get(reverse('pets-medical-history-get', args=[pet.pet_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar se os dados retornados estão corretos
        self.assertEqual(response.data['pet']['nome'], pet.nome)

class PetMedicalHistoryVacinaTestCase(PetApiTestBase):
    
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        # Adicionar uma vacina como exemplo
        cls.vacina = Vacinas.objects.create(nome="Vacina Exemplo")

    def test_add_vacina_administrada(self):
        # Registrar o pet
        response = self.client.post(reverse('pets-register'), self.pet_data, format='json')
        pet = Pet.objects.first()
        medical_history = HistoricoMedico.objects.filter(pet=pet).first()

        # Dados da vacina administrada
        vacina_data = {
            "observacao": "Vacina administrada com sucesso",
            "data_aplicacao": "2024-10-21T02:43:37.669Z",
            "data_reforco": "2024-10-21T02:43:37.669Z",
            "vacina": f"{self.vacina.vacina_id}",
            "historico_medico": f"{medical_history.historico_medico_id}",
        }

        # Adicionar a vacina administrada
        response = self.client.post(reverse('pets-medical-history-vacinas-add-vacina'), vacina_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificar se a vacina foi administrada corretamente
        vacina_administrada = VacinasAdministradas.objects.first()
        self.assertEqual(VacinasAdministradas.objects.count(), 1)
        self.assertEqual(vacina_administrada.vacina.nome, self.vacina.nome)
        self.assertEqual(vacina_administrada.historico_medico.historico_medico_id, medical_history.historico_medico_id)
    
    def test_remove_vacina_administrada(self):
        # Registrar o pet
        self.client.post(reverse('pets-register'), self.pet_data, format='json')
        pet = Pet.objects.first()
        medical_history = HistoricoMedico.objects.filter(pet=pet).first()

        # Adicionar a vacina administrada
        vacina_data = {
            "observacao": "Vacina administrada com sucesso",
            "data_aplicacao": "2024-10-21T02:43:37.669Z",
            "data_reforco": "2024-10-21T02:43:37.669Z",
            "vacina": f"{self.vacina.vacina_id}",
            "historico_medico": f"{medical_history.historico_medico_id}",
        }
        self.client.post(reverse('pets-medical-history-vacinas-add-vacina'), vacina_data, format="json")

        # Verificar se a vacina foi adicionada corretamente
        vacina_administrada = VacinasAdministradas.objects.first()
        self.assertEqual(VacinasAdministradas.objects.count(), 1)

        # Fazer uma requisição DELETE para remover a vacina administrada
        response = self.client.delete(reverse('pets-medical-history-vacinas-delete-vacina', args=[vacina_administrada.vacinas_administradas_id]))

        # Verificar se a resposta é HTTP 204 NO CONTENT
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verificar se a vacina foi removida do banco de dados
        self.assertEqual(VacinasAdministradas.objects.count(), 0)
