from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import login

User = get_user_model()

class AccountAuthenticatedViewSetTests(APITestCase):

    def setUp(self):
        # Cria um usuário para os testes de autenticação
        self.user = User.objects.create_user(username="testuser", email="testuser@example.com", password="password123")
        self.client.login(email="testuser@example.com", password="password123")  # Faz o login no client para os testes

    def test_get_account(self):
        # Testa o endpoint GET para retornar os dados do usuário autenticado
        url = reverse('accountauthenticated-get')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"username": "testuser", "email": "testuser@example.com"})

    def test_update_account(self):
        # Testa o endpoint PUT para atualizar os dados do usuário autenticado
        url = reverse('accountauthenticated-update')
        data = {"username": "updateduser", "email": "updateduser@example.com"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        # Verifica se os dados foram realmente atualizados no banco
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, "updateduser")
        self.assertEqual(self.user.email, "updateduser@example.com")

    def test_change_password(self):
        # Testa o endpoint PUT para trocar a senha do usuário autenticado
        url = reverse('accountauthenticated-change-password')
        data = {"password": "newpassword123"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        # Tenta fazer login com a nova senha para verificar a atualização
        self.client.logout()
        login_successful = self.client.login(email=self.user.email, password="newpassword123")
        self.assertTrue(login_successful, "Não foi possível fazer login com a nova senha")

    def test_logout(self):
        # Testa o endpoint POST para logout
        url = reverse('accountauthenticated-logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
        
        # Verifica se o usuário foi deslogado
        response = self.client.get(reverse('accountauthenticated-get'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Acesso negado, pois o usuário está deslogado
