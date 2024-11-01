# from rest_framework import status
# from rest_framework.test import APITestCase
# from django.urls import reverse
# from account.models import AppAccount

# class AccountNotAuthenticatedTests(APITestCase):
    
#     def setUp(self):
#         # Criação de um usuário de teste
#         self.user_data = {
#             "email": "testuser@example.com",
#             "password": "strongpassword123",
#             "username": "testuser"
#         }
#         self.user = AppAccount.objects.create_user(**self.user_data)
    
#     def test_register_user(self):
#         url = reverse('accountnotauthenticated-register')
#         data = {
#             "email": "newuser@example.com",
#             "password": "newpassword123",
#             "username": "newuser"
#         }
#         response = self.client.post(url, data, format='json')
        
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(AppAccount.objects.filter(email="newuser@example.com").exists(), True)
    
#     def test_login_user(self):
#         url = reverse('accountnotauthenticated-login')
#         data = {
#             "email": self.user_data["email"],
#             "password": self.user_data["password"]
#         }
#         response = self.client.post(url, data, format='json')
        
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('_auth_user_id', self.client.session)

#     def test_request_password_reset(self):
#         url = reverse('accountnotauthenticated-request-password-reset')
#         data = {"email": self.user_data["email"]}
#         redirect_url = "http://example.com/reset"
        
#         response = self.client.post(f'{url}?redirect={redirect_url}', data, format='json')

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('If the email is registered', response.data['detail'])

#     def test_reset_password(self):
#         url = reverse('accountnotauthenticated-reset-password')
#         self.client.force_authenticate(user=self.user)
#         data = {
#             "password": "newpassword123",
#             "confirm_password": "newpassword123"
#         }
#         response = self.client.post(url, data, format='json')

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('Password reset successfully', response.data['detail'])

# class AccountAuthenticatedTests(APITestCase):

#     def setUp(self):
#         # Criação de um usuário de teste e autenticação
#         self.user_data = {
#             "email": "authuser@example.com",
#             "password": "strongpassword123",
#             "username": "authuser"
#         }
#         self.user = AppAccount.objects.create_user(**self.user_data)
#         self.client.login(email=self.user_data["email"], password=self.user_data["password"])

#     def test_get_user_auth(self):
#         url = reverse('accountauthenticated-get-user-auth')
#         response = self.client.get(url, format='json')
        
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["email"], self.user_data["email"])

#     def test_update_user(self):
#         url = reverse('accountauthenticated-update-account')
#         data = {
#             "email": "updateduser@example.com",
#             "username": "updateduser"
#         }
#         response = self.client.put(url, data, format='json')

#         self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
#         self.user.refresh_from_db()
#         self.assertEqual(self.user.email, "updateduser@example.com")

#     def test_change_password(self):
#         url = reverse('accountauthenticated-change-password')
#         data = {
#             "password": "newpassword123"
#         }
#         response = self.client.put(url, data, format='json')

#         self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
#         self.assertIn('Password changed successfully', response.data['detail'])
#         self.client.logout()

#     def test_logout(self):
#         # Autenticar o usuário antes de tentar fazer logout
#         self.client.force_authenticate(user=self.user)

#         # Fazer a requisição de logout
#         response = self.client.post(reverse('accountauthenticated-logout'))

#         # Verificar se a resposta foi HTTP 205 (Reset Content), que é o que você espera para um logout bem-sucedido
#         self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)