from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from pet.models import Pet, HistoricoMedico, Vacinas, VacinasAdministradas
from pet_owners.models import PetOwners
from account.models import AppAccount

class PetApiTestCase(APITestCase):
    def setUp(self) -> None:
        default_email = "user@example.com"
        
        self.account = AppAccount.objects.create(email=default_email, username="user")
        self.account.set_password('password')
        
        self.owner = PetOwners.objects.create(nome='User', email=default_email)
        
        # Autenticando o usuário
        self.client.force_authenticate(self.account)
        
    def test_register_pet(self):
        
        data = {
            "nome": "Bobby",
            "especie": "Cachorro",
            "raca": "Poodle",
            "peso": 12.5,
            "idade": 3,
            "sexo": "M",
            "pet_owner": self.owner.id_pet_owners
        }   
        
        # Faz uma requisição POST para a rota de registro com os dados do pet
        response = self.client.post(reverse('pets-register'), data, format='json')      
        
        # Verifica se a resposta foi HTTP 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verifica se o pet foi criado
        self.assertEqual(Pet.objects.count(), 1)
        
        # Verifica se o historico medico foi criado
        self.assertEqual(HistoricoMedico.objects.count(), 1)
        
        pet = Pet.objects.first()
        
        # Verifica se o pet foi vinculado corretamente ao dono do pet (petonwer)
        self.assertEqual(pet.pet_owner.email, self.owner.email)
        
        # Verifica se os dados foram adiconados corretamente
        self.assertEqual(pet.nome, data['nome'])
        
class PetApiTesteCaseGet(APITestCase):
    def setUp(self) -> None:
        default_email = "user@example.com"
        
        self.account = AppAccount.objects.create(email=default_email, username="user")
        self.account.set_password('password')
        self.account.save()  # Salve o usuário para que a senha seja aplicada
        
        self.owner = PetOwners.objects.create(nome='User', email=default_email)
        
        # Autenticando o usuário
        self.client.force_authenticate(self.account)

        self.pet_data = {
            "nome": "Bobby",
            "especie": "Cachorro",
            "raca": "Poodle",
            "peso": 12.5,
            "idade": 3,
            "sexo": "M",
            "pet_owner": self.owner.id_pet_owners
        }

        # Faz a requisição POST para criar o pet
        self.client.post(reverse('pets-register'), self.pet_data, format='json')
        
    def test_get_pet(self):
        
        # Obtém o pet que foi criado no setUp
        pet = Pet.objects.first()

        # Faz uma requisição GET para a rota de obter o pet
        response = self.client.get(reverse('pets-get', args=[pet.pet_id]))  # Ajuste a URL conforme necessário

        # Verifica se a resposta foi HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se os dados retornados estão corretos
        self.assertEqual(response.data['nome'], pet.nome)
        self.assertEqual(response.data['especie'], pet.especie)
        self.assertEqual(response.data['raca'], pet.raca)
        self.assertEqual(float(response.data['peso']), float(pet.peso))
        self.assertEqual(response.data['idade'], pet.idade)
        self.assertEqual(response.data['sexo'], pet.sexo)

        # Verifica se o pet owner é o correto
        self.assertEqual(response.data['pet_owner'], self.owner.id_pet_owners)
        
class PetApiTestCaseUpdate(APITestCase):
    def setUp(self) -> None:
        default_email = "user@example.com"
        
        self.account = AppAccount.objects.create(email=default_email, username="user")
        self.account.set_password('password')
        self.account.save()  # Salve o usuário para que a senha seja aplicada
        
        self.owner = PetOwners.objects.create(nome='User', email=default_email)
        
        # Autenticando o usuário
        self.client.force_authenticate(self.account)

        self.pet_data = {
            "nome": "Bobby",
            "especie": "Cachorro",
            "raca": "Poodle",
            "peso": 12.5,
            "idade": 3,
            "sexo": "M",
            "pet_owner": self.owner.id_pet_owners
        }

        # Faz a requisição POST para criar o pet
        self.client.post(reverse('pets-register'), self.pet_data, format='json')
        
    def test_update_pet(self):
        pet = Pet.objects.first()
        
        data = {
            "nome": "Bobby UPDATED",
            "especie": "Cachorro",
            "raca": "Poodle",
            "peso": 12.5,
            "idade": 3,
            "sexo": "M",
        }
         
        response = self.client.put(reverse('pets-update', args=[pet.pet_id]), data)

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data['nome'], data['nome'])
        
class PetApiTestCaseDelete(APITestCase):
    def setUp(self) -> None:
        default_email = "user@example.com"
        
        self.account = AppAccount.objects.create(email=default_email, username="user")
        self.account.set_password('password')
        self.account.save()  # Salve o usuário para que a senha seja aplicada
        
        self.owner = PetOwners.objects.create(nome='User', email=default_email)
        
        # Autenticando o usuário
        self.client.force_authenticate(self.account)

        self.pet_data = {
            "nome": "Bobby",
            "especie": "Cachorro",
            "raca": "Poodle",
            "peso": 12.5,
            "idade": 3,
            "sexo": "M",
            "pet_owner": self.owner.id_pet_owners
        }

        # Faz a requisição POST para criar o pet
        self.client.post(reverse('pets-register'), self.pet_data, format='json')
        
        self.pet = Pet.objects.first()
        
    def test_delete_pet(self):
        # Verifica se o pet foi criado
        self.assertEqual(Pet.objects.count(), 1)

        # Faz uma requisição DELETE para a rota de exclusão
        response = self.client.delete(reverse('pets-delete', args=[self.pet.pet_id]))

        # Verifica se a resposta foi HTTP 204 NO CONTENT
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verifica se o pet foi realmente excluído
        self.assertEqual(Pet.objects.count(), 0)
        
        # Verifica se o historico do pet foi excluido tambem
        self.assertEqual(HistoricoMedico.objects.count(), 0)
        
class PetMedicalHistoryTestCaseGet(APITestCase):
    def setUp(self) -> None:
        default_email = "user@example.com"
        
        self.account = AppAccount.objects.create(email=default_email, username="user")
        self.account.set_password('password')
        self.account.save()  # Salve o usuário para que a senha seja aplicada
        
        self.owner = PetOwners.objects.create(nome='User', email=default_email)
        
        # Autenticando o usuário
        self.client.force_authenticate(self.account)

        self.pet_data = {
            "nome": "Bobby",
            "especie": "Cachorro",
            "raca": "Poodle",
            "peso": 12.5,
            "idade": 3,
            "sexo": "M",
            "pet_owner": self.owner.id_pet_owners
        }

        # Faz a requisição POST para criar o pet
        self.client.post(reverse('pets-register'), self.pet_data, format='json')
        
        self.pet = Pet.objects.first()
        
    def test_get_medical_history(self):
        response = self.client.get(reverse('pets-medical-history-get', args=[self.pet.pet_id]))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se os dados retornados estão corretos
        self.assertEqual(response.data['pet']['nome'], self.pet.nome)
        
class PetMedicalHistoryVacinaTesteCaseAdd(APITestCase):
    def setUp(self) -> None:
        default_email = "user@example.com"
        
        self.account = AppAccount.objects.create(email=default_email, username="user")
        self.account.set_password('password')
        self.account.save()  # Salve o usuário para que a senha seja aplicada
        
        self.owner = PetOwners.objects.create(nome='User', email=default_email)
        
        # Autenticando o usuário
        self.client.force_authenticate(self.account)

        self.pet_data = {
            "nome": "Bobby",
            "especie": "Cachorro",
            "raca": "Poodle",
            "peso": 12.5,
            "idade": 3,
            "sexo": "M",
            "pet_owner": self.owner.id_pet_owners
        }

        # Faz a requisição POST para criar o pet
        self.client.post(reverse('pets-register'), self.pet_data, format='json')
        
        self.pet = Pet.objects.first()
        
        self.medical_history = HistoricoMedico.objects.filter(pet = self.pet).first()
        
        self.vacina = Vacinas.objects.create(nome="example")
        
    def test_add_vacina_administrada(self):
        data = {
            "observacao": "string",
            "data_aplicacao": "2024-10-21T02:43:37.669Z",
            "data_reforco": "2024-10-21T02:43:37.669Z",
            "vacina": f"{self.vacina.vacina_id}",
            "historico_medico": f"{self.medical_history.historico_medico_id}",
        }
        
        response = self.client.post(reverse('pets-medical-history-vacinas-add-vacina'),data, format="json")
        
        vacina_administrada = VacinasAdministradas.objects.first()
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VacinasAdministradas.objects.count(), 1)
        self.assertEqual(vacina_administrada.vacina.nome, self.vacina.nome)
        self.assertAlmostEqual(vacina_administrada.historico_medico.historico_medico_id, self.medical_history.historico_medico_id)