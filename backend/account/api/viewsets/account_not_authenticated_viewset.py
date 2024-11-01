from django.contrib.auth import logout, login, authenticate
from django.core.mail import send_mail
from rest_framework import permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from decouple import config
from rest_framework import viewsets, mixins
from pet_care_backend.utils import ResponseMixin
from pet_care_backend.utils import HttpResponseUtils as http
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from drf_yasg import openapi
from ..serializers import AccountCreateSerializer, AccountLoginSerializer, AccountRequestPasswordResetSerializer, AccountChangePasswordSerializer

class AccountNotAuthenticatedViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet, ResponseMixin):
    def get_serializer_class(self):
        action_serializers = {
            "login": AccountLoginSerializer,
            "request_password_reset": AccountRequestPasswordResetSerializer,
            "reset_password": AccountChangePasswordSerializer
        }
        return action_serializers.get(self.action, AccountCreateSerializer)
    
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
    @action(detail=False, methods=['post'], url_name='request-password-reset')
    def request_password_reset(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.get_user()
            redirect_url = request.query_params.get('redirect')
            
            if not redirect_url:
                return http.response('Redirect URL is required.', status.HTTP_400_BAD_REQUEST)

            if user:
                token = RefreshToken.for_user(user)
                reset_link = f"{redirect_url}?token={str(token.access_token)}"
                send_mail(
                    'Redefinição de senha',
                    f'Acesse esse link para redefinir a sua senha: {reset_link}',
                    config('EMAIL_HOST_USER'),
                    [user.email]
                )
                return http.response('If the email is registered, you will receive a link to reset your password.')
    
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
    @action(detail=False, methods=['post'], url_name='reset-password', permission_classes=[permissions.IsAuthenticated], authentication_classes=[JWTAuthentication])
    def reset_password(self, request):
        serializer = self.get_serializer(data=request.data, instance=request.user)
        saved_user = self.handle_serializer_errors(serializer)
        if saved_user:
            return http.response('Password reset successfully.')
    
    @action(detail=False, methods=['post'], url_name='login')
    def login(self,request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email=email, password=password)
            
            if user is not None:
                login(request, user)
                return http.response_empty()
            return http.response('Invalid credentials', status.HTTP_401_UNAUTHORIZED)