from rest_framework.test import APITestCase
from pet_owners.models import PetOwners
from account.models import AppAccount

class PetApiTestBase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        default_email = "user@example.com"
        
        cls.account = AppAccount.objects.create(email=default_email, username="user")
        cls.account.set_password('password')
        cls.account.save()

        cls.owner = PetOwners.objects.create(nome='User', email=default_email)
        
        cls.pet_data = {
            "nome": "Bobby",
            "especie": "Cachorro",
            "raca": "Poodle",
            "peso": 12.5,
            "idade": 3,
            "sexo": "M",
            "pet_owner": cls.owner.id_pet_owner
        }

    def setUp(self):
        self.client.force_authenticate(self.account)
    
    def _verify_pet_data(self, response_data, expected_data):
        self.assertEqual(response_data['nome'], expected_data['nome'])
        self.assertEqual(response_data['especie'], expected_data['especie'])
        self.assertEqual(response_data['raca'], expected_data['raca'])
        self.assertEqual(float(response_data['peso']), float(expected_data['peso']))
        self.assertEqual(response_data['idade'], expected_data['idade'])
        self.assertEqual(response_data['sexo'], expected_data['sexo'])
