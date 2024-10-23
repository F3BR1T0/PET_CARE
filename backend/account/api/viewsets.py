from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth import logout, login, authenticate
from django.core.mail import send_mail
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from decouple import config

from account.api import serializers
from pet_care_backend.utils import HttpResponseUtils as httputils
from account.models import AppAccount

class ResponseMixin:
    def handle_serializer_errors(self, serializer):
        if serializer.is_valid(raise_exception=True):
            try:
                return serializer.save()
            except Exception as e:
                return httputils.response_bad_request_400(str(e))
        return httputils.response_as_json(serializer.errors, status.HTTP_400_BAD_REQUEST)

class AccountAdminViewSet(viewsets.ModelViewSet, ResponseMixin):
    permission_classes = [permissions.IsAuthenticated & permissions.IsAdminUser]
    authentication_classes = [SessionAuthentication]
    serializer_class = serializers.AccountSerializer
    queryset = AppAccount.objects.all()

    def get_serializer_class(self):
        if self.action == "change_password_as_admin":
            return serializers.AccountChangePasswordSerializer
        return super().get_serializer_class()

    def partial_update(self, request):
        return httputils.response_bad_request_400("not implemented")

    def create(self, request):
        return httputils.response_bad_request_400("not implemented")
    
    @action(detail=True, methods=['put'],url_path='change-password-as-admin')
    def change_password_as_admin(self, request, pk: None):
        user = self.get_queryset().filter(id=pk).first()
        serializer = self.get_serializer(data=request.data, instance=user)

        if user:
            saved_user = self.handle_serializer_errors(serializer)
            if saved_user:
                return httputils.response("Password changed successfully", status.HTTP_202_ACCEPTED)
        return httputils.response_bad_request_400("User not found.")
        
class AccountNotAuthenticatedViewSet(viewsets.GenericViewSet, ResponseMixin):
    serializer_class = serializers.AccountRegisterSerializer
    
    def get_serializer_class(self):
        action_serializers = {
            "register": serializers.AccountRegisterSerializer,
            "login": serializers.AccountLoginSerializer,
            "request_password_reset": serializers.AccountRequestPasswordResetSerializer,
            "reset_password": serializers.AccountChangePasswordSerializer
        }
        return action_serializers.get(self.action, super().get_serializer_class())
    
    @swagger_auto_schema(
        methods=['post'],
        operation_description="Solicita a redefinição de senha. Um URL de redirecionamento pode ser fornecido.",
        manual_parameters=[
            openapi.Parameter(
                'redirect',
                openapi.IN_QUERY,
                description="URL para redirecionamento após a redefinição de senha.",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={200: 'Success', 400: 'Bad Request'}
    )
    @action(detail=False, methods=['post'], url_name='request-password-reset', url_path='request-password-reset')
    def request_password_reset(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.get_user()
            redirect_url = request.query_params.get('redirect')
            
            if not redirect_url:
                return httputils.response('Redirect URL is required.', status.HTTP_400_BAD_REQUEST)

            if user:
                token = RefreshToken.for_user(user)
                reset_link = f"{redirect_url}?token={str(token.access_token)}"
                send_mail(
                    'Redefinição de senha',
                    f'Acesse esse link para redefinir a sua senha: {reset_link}',
                    config('EMAIL_HOST_USER'),
                    [user.email]
                )
                return httputils.response('If the email is registered, you will receive a link to reset your password.')
    
    @swagger_auto_schema(
        methods=['post'],
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description="Api Key no formato: `Bearer <token>`",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={200: 'Success', 400: 'Bad Request'}
    )            
    @action(detail=False, methods=['post'], url_name='reset-password', url_path='reset-password', permission_classes=[permissions.IsAuthenticated], authentication_classes=[JWTAuthentication])
    def reset_password(self, request):
        serializer = self.get_serializer(data=request.data, instance=request.user)
        saved_user = self.handle_serializer_errors(serializer)
        if saved_user:
            return httputils.response('Password reset successfully.')
    
    @action(detail=False, methods=['post'], url_name='register')
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        saved_user = self.handle_serializer_errors(serializer)
        if saved_user:
            return httputils.response_as_json(serializer.data, status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'], url_name='login', url_path='login')
    def login(self,request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)
                return httputils.response_empty()
            return httputils.response('Invalid credentials', status.HTTP_401_UNAUTHORIZED)

class AccountAuthenticatedViewSet(viewsets.GenericViewSet, ResponseMixin):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    serializer_class = serializers.AccountUpdateSerializer
    
    def get_serializer_class(self):
        action_serializers = {
            "change_password": serializers.AccountChangePasswordSerializer
        }
        return action_serializers.get(self.action, super().get_serializer_class())
    
    @action(detail=False, methods=['get'], url_path="get-user-auth")
    def get_user_auth(self,request):
        return httputils.response_as_json({
            'username': request.user.username,
            'email': request.user.email
        })
    
    @action(detail=False, methods=['put'], url_path="update-account")
    def update_account(self, request):
        serializer = self.get_serializer(instance=request.user, data=request.data)
        saved_user = self.handle_serializer_errors(serializer)
        if saved_user:
            return httputils.response_as_json(serializer.data, status.HTTP_202_ACCEPTED)
    
    @action(detail=False, methods=['put'], url_path="change-password")
    def change_password(self, request):
        serializer = self.get_serializer(data=request.data, instance=request.user)
        saved_user = self.handle_serializer_errors(serializer)
        if saved_user:
            logout(request)
            return httputils.response('Password changed successfully', status.HTTP_202_ACCEPTED)
    
    @action(detail=False, methods=['post'], url_path="logout")
    def logout(self, request):
        try:
            logout(request)
            return httputils.response('Logout completed successfully',status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return httputils.response_bad_request_400(str(e))