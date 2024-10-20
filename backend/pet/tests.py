from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from pet.models import Pet, HistoricoMedico
from pet_owners.models import PetOwners
from account.models import AppAccount

class PetApiTestCase(APITestCase):
    def setUp(self) -> None:
        default_email = "user@example.com"
        
        self.account = AppAccount.objects.create(email=default_email, username="user")
        self.account.set_password('password')
        
        self.owner = PetOwners.objects.create(nome='User', email=default_email)
        
        self.url = reverse('pets-register')
        
    def test_register_pet(self):
        
        # Autenticando o usuário
        self.client.force_authenticate(self.account)
        
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
        response = self.client.post(self.url, data, format='json')      
        
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