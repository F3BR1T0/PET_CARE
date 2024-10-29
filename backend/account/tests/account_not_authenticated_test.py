from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from account.models import AppAccount

class AccountNotAuthenticatedTests(APITestCase):
    
    def setUp(self) -> None:
        self.account = AppAccount.objects.create(username='example', email='example@gmail.com')
        self.account.set_password('password')
        self.account.save()
    
    def test_login_account(self):
        url = reverse('accountnotauthenticated-login')
        data = {
            "email": "example@gmail.com",
            "password": "password",
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('_auth_user_id', self.client.session)
    
    def test_request_password_reset(self):
        url = reverse('accountnotauthenticated-request-password-reset')
        data = {"email": "example@gmail.com"}
        redirect_url = "http://example.com/reset"
        
        response = self.client.post(f'{url}?redirect={redirect_url}', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('If the email is registered', response.data['detail'])
        
    def test_reset_password(self):
        url = reverse('accountnotauthenticated-reset-password')
        self.client.force_authenticate(user=self.account)
        data = {
            "password": "newpassword123",
            "confirm_password": "newpassword123"
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Password reset successfully', response.data['detail'])
    
