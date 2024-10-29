from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from ..models import PetOwner, Address

User = get_user_model()

class BaseApiTestCase(APITestCase):
    def setUp(self):
        # Configuração inicial: cria um usuário e um pet owner para os testes
        self.user = User.objects.create_user(username="testuser", email="testuser@example.com", password="password123")
        self.pet_owner = PetOwner.objects.create(nome=self.user.username, email=self.user.email)
        self.client.login(email=self.user.email, password="password123")