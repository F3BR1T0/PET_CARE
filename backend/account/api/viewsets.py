from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth import logout, login, authenticate
from django.core.mail import send_mail
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from decouple import config

from account.api.serializers import AccountRegisterSerializer, AccountDefaultSerializer, AccountLoginSerializer, AccountLogoutSerializer, AccountResetPasswordSerializer, AccountRequestPasswordResetSerializer, AccountUpdateSerializer, AccountChangePasswordSerializer
from pet_care_backend.utils import HttpResponseUtils as httputils
from account.models import AppAccount

class AccountViewSet(viewsets.ModelViewSet):    
    serializer_class = AccountDefaultSerializer
    queryset = AppAccount.objects.all()

    def get_queryset(self):
        return super().get_queryset()
    
    def get_serializer_class(self):
        if self.action in ("register", "create"):
            return AccountRegisterSerializer
        if self.action == "login":
            return AccountLoginSerializer
        if self.action == "logout":
            return AccountLogoutSerializer
        if self.action == "reset_password":
            return AccountResetPasswordSerializer
        if self.action == "request_password_reset":
            return AccountRequestPasswordResetSerializer
        if self.action == "update_account":
            return AccountUpdateSerializer
        if self.action in ("change_password", "change_password_as_admin"):
            return AccountChangePasswordSerializer
        return super().get_serializer_class()
    
    def list(self, request):
        self.__check_if_is_admin(request)
        return super().list(request) 
    
    def retrieve(self, request, pk:None):
        self.__check_if_is_admin(request)
        return super().retrieve(request, pk)
    
    def update(self, request, pk:None):
        self.__check_if_is_admin(request)
        return super().update(request, pk)
    
    def partial_update(self, request):
        self.__check_if_is_admin(request)
        return httputils.response_bad_request_400("not implemented")

    def create(self, request):
        self.__check_if_is_admin(request)
        return httputils.response_bad_request_400("not implemented")
    
    def destroy(self, request, pk: None):
        self.__check_if_is_admin(request)
        return super().destroy(request, pk)
    
    @action(detail=True, methods=['put'],url_path='change-password-as-admin', permission_classes=[permissions.IsAuthenticated, permissions.IsAdminUser], authentication_classes=[SessionAuthentication])
    def change_password_as_admin(self, request, pk: None):
        self.__check_if_is_admin(request)
        user = self.get_queryset().filter(id=pk).first()
        serializer = self.get_serializer(data=request.data, instance=user)

        if serializer.is_valid(raise_exception=True):
            try:
                user = serializer.save()
                if user:
                    return httputils.response('Password changed successfully', status.HTTP_202_ACCEPTED)
            except Exception as e:
                return httputils.response_bad_request_400(str(e))
            return httputils.response_as_json(serializer.errors, status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_name='register')
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                user = serializer.create(request.data)
                if user:
                    return httputils.response_as_json(serializer.data, status.HTTP_201_CREATED)
            except Exception as e:
                return httputils.response_bad_request_400(str(e))
        return httputils.response_as_json(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    @action(detail=False, methods=['post'], url_name='logout', permission_classes=[permissions.IsAuthenticated], authentication_classes=[SessionAuthentication])
    def logout(self, request):
        try:
            logout(request)
            return httputils.response('Logout completed successfully',status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return httputils.response_bad_request_400(str(e))
        
        
        
    @action(detail=False, methods=['post'], url_name='login')
    def login(self,request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email=email, password=password)
        
            if user is not None:
                login(request, user)
                return httputils.response_empy()
            else:
                return httputils.response('Invalid credentials', status.HTTP_401_UNAUTHORIZED)
        return httputils.response_as_json(serializer.errors,status.HTTP_400_BAD_REQUEST)
        
    
    @action(detail=False, methods=['get'], url_name='getme', permission_classes=[permissions.IsAuthenticated], authentication_classes=[SessionAuthentication])
    def getme(self, request):
        return httputils.response_as_json({'id': request.user.id,'username': request.user.username,'email': request.user.email})
        

    @action(detail=False, methods=['post'], url_name='request password reset', url_path='request-password-reset')
    def request_password_reset(self, request):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            try:
                user = serializer.get_user()
                redirect_url = request.query_params.get('redirect')
            
                if not redirect_url:
                    return httputils.response('Redirect URL is required.',status.HTTP_400_BAD_REQUEST)
            
                if user:
                    # Gerar o token
                    token = RefreshToken.for_user(user)
                    redirect_url = f"{redirect_url}?token={str(token.access_token)}"
                
                    # Enviar email
                    send_mail(
                        'Redefinição de senha',
                        f'Acesse esse link para redefinir a sua senha: {redirect_url}',
                        config('EMAIL_HOST_USER'),
                        [user.email]
                    )
                
                    return httputils.response('If the email is registered, you will receive a link to reset your password.')
            except Exception as e:
                return httputils.response_bad_request_400(str(e))
        return httputils.response_as_json(serializer.errors,status.HTTP_400_BAD_REQUEST)
            
    
    @action(detail=False, methods=['post'], url_name='reset_password', url_path='reset-password', permission_classes=[permissions.IsAuthenticated], authentication_classes=[JWTAuthentication])
    def reset_password(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save(request.user.id)
                return httputils.response('Password reset successfully.')
            except Exception as e:
                return httputils.response(str(e), status.HTTP_400_BAD_REQUEST)
        return httputils.response_as_json(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['put'], url_name='update', permission_classes=[permissions.IsAuthenticated], authentication_classes=[SessionAuthentication])
    def update_account(self, request):
        serializer = self.get_serializer(instance=request.user, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            try:
                user = serializer.save()
                if user:
                    return httputils.response_as_json(serializer.data, status.HTTP_202_ACCEPTED)
            except Exception as e:
                return httputils.response_bad_request_400(str(e))
        return httputils.response_as_json(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['put'], url_name='change password', permission_classes=[permissions.IsAuthenticated], authentication_classes=[SessionAuthentication])
    def change_password(self, request):
        serializer = self.get_serializer(data=request.data, instance=request.user)
        
        if serializer.is_valid(raise_exception=True):
            try:
                user = serializer.save()
                if user:
                    logout(request)
                    return httputils.response('Password changed successfully', status.HTTP_202_ACCEPTED)
            except Exception as e:
                return httputils.response_bad_request_400(str(e))
            return httputils.response_as_json(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    def __check_if_is_admin(self,request):
        self.permission_classes = [IsAuthenticated, IsAdminUser]
        self.check_permissions(request)
    
