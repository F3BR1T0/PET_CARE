from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth import logout, login, authenticate
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from account.api.serializers import AccountRegisterSerializer, AccountDefaultSerializer, AccountLoginSerializer, AccountResetPasswordSerializer, AccountRequestPasswordResetSerializer
from account.models import AppAccount
from pet_care_backend.utils import HttpResponseUtils as httputils

class AccountViewSet(viewsets.ModelViewSet):    
    serializer_class = AccountDefaultSerializer
    queryset = AppAccount.objects.none()
    
    def get_serializer_class(self):
        if self.action == "register":
            return AccountRegisterSerializer
        if self.action == "login":
            return AccountLoginSerializer
        if self.action == "reset_password":
            return AccountResetPasswordSerializer
        if self.action == "request_password_reset":
            return AccountRequestPasswordResetSerializer
        return super().get_serializer_class()


    @action(detail=False, methods=['post'], url_name='register')
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)
            if user:
                return httputils.response_as_json(serializer.data, status.HTTP_201_CREATED)
        return httputils.response_as_json(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    @action(detail=False, methods=['post'], url_name='logout', permission_classes=[permissions.IsAuthenticated], authentication_classes=[SessionAuthentication])
    def logout(self, request):
        try:
            logout(request)
            return httputils.response('Logout completed successfully',status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return httputils.response(str(e), status.HTTP_400_BAD_REQUEST)
        
        
        
    @action(detail=False, methods=['post'], url_name='login')
    def login(self,request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email=email, password=password)
        
            if user is not None:
                login(request, user)
                return self.response_empy()
            else:
                return self.response('Invalid credentials', status.HTTP_401_UNAUTHORIZED)
        return self.response_as_json(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    
    @action(detail=False, methods=['get'], url_name='getme', permission_classes=[permissions.IsAuthenticated], authentication_classes=[SessionAuthentication])
    def getme(self, request):
        return self.response_as_json({'id': request.user.id,'username': request.user.username,'email': request.user.email})
        

    @action(detail=False, methods=['post'], url_name='request password reset', url_path='request-password-reset')
    def request_password_reset(self, request):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.get_user()
            redirect_url = request.query_params.get('redirect')
            
            if not redirect_url:
                return self.response('Redirect URL is required.',status.HTTP_400_BAD_REQUEST)
            
            if user:
                # Gerar o token
                token = RefreshToken.for_user(user)
                redirect_url = f"{redirect_url}?token={str(token.access_token)}"
                
                # Enviar email
                
                return self.response('If the email is registered, you will receive a link to reset your password.')
        return self.response_as_json(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
    
    @action(detail=False, methods=['post'], url_name='reset_password', url_path='reset-password', permission_classes=[permissions.IsAuthenticated], authentication_classes=[JWTAuthentication])
    def reset_password(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save(request.user.id)
                return self.response('Password reset successfully.')
            except Exception as e:
                return self.response(str(e), status.HTTP_400_BAD_REQUEST)
        return self.response_as_json(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
