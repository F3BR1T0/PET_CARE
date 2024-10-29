from .base_test import *

User = get_user_model()

class PetOwnerAddressViewSetTests(BaseApiTestCase):
    
    def test_create_address(self):
        # Testa o endpoint para criar um endereço de PetOwner
        url = reverse('petowner-address-create-address')
        
        data = {
            "cidade": "Cidade teste",
            "estado": "São Paulo",
            "pais": "Brasil",
            "cep": "10020036"
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Tenta criar o endereço novamente, agora que o PetOwner já possui um
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Already have a address", response.data['error'])

    def test_update_address(self):
        # Configuração inicial: cria um endereço para o PetOwner
        address = Address.objects.create(cidade="string", estado="estado", pais="strng", cep="10030035")
        self.pet_owner.endereco = address
        self.pet_owner.save()
        
        # Testa o endpoint para atualizar o endereço de PetOwner
        url = reverse('petowner-address-update-address')
        updated_data = {
            "cidade": "update",
            "estado": "update",
            "pais": "update",
            "cep": "11111111"
        }

        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        # Verifica se o endereço foi realmente atualizado no banco
        self.pet_owner.refresh_from_db()
        self.assertEqual(self.pet_owner.endereco.cidade, updated_data['cidade'])
        self.assertEqual(self.pet_owner.endereco.cep, updated_data['cep'])
