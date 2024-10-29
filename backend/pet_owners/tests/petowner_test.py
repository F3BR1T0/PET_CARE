from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from ..models import PetOwner
import json

User = get_user_model()

class PetOwnerViewSetTests(APITestCase):

    def setUp(self):
        # Configuração inicial: cria um usuário e um pet owner para os testes
        self.user = User.objects.create_user(username="testuser", email="testuser@example.com", password="password123")
        self.pet_owner = PetOwner.objects.create(nome=self.user.username, email=self.user.email)
        self.client.login(email=self.user.email, password="password123")
        self.data = {"nome": "user updated", "email": "updateduser@example.com", "foto": "3x4", "cpf":"99999999999", "telefone":"40028922" }

    def test_update_petowner(self):
        # Testa o endpoint de atualização de PetOwner
        url = reverse('petowner-update')

        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        
        # Verifica se o email foi realmente atualizado no banco de dados
        self.user.refresh_from_db()
        self.pet_owner.refresh_from_db()
        self.assertEqual(self.user.email, "updateduser@example.com")
        self.assertEqual(self.pet_owner.email, self.user.email)

    def test_get_petowner(self):
        # Testa o endpoint de obter dados de PetOwner
        url = reverse('petowner-get')

        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], self.user.username)
        self.assertEqual(response.data["email"], self.user.email)

    def test_delete_petowner(self):
        # Testa o endpoint de exclusão de PetOwner
        url = reverse('petowner-delete')

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verifica se o usuário e o PetOwner foram realmente deletados
        self.assertFalse(User.objects.filter(id=self.user.id).exists())
        self.assertFalse(PetOwner.objects.filter(email=self.user.email).exists())
