from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import logout, login, authenticate
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication

from account.api.serializers import AccountRegisterSerializer, AccountDefaultSerializer, AccountLoginSerializer
from account.models import AppAccount

class AccountViewSet(viewsets.ModelViewSet):    
    serializer_class = AccountDefaultSerializer
    queryset = AppAccount.objects.none()
    
    def get_serializer_class(self):
        if self.action == "register":
            return AccountRegisterSerializer
        if self.action == "login":
            return AccountLoginSerializer
        return super().get_serializer_class()

    @action(detail=False, methods=['post'], url_name='register')
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'], url_name='logout', permission_classes=[permissions.IsAuthenticated], authentication_classes=[SessionAuthentication])
    def logout(self, request):
        try:
            logout(request)
            return Response({'detail': 'Logout realizado com sucesso'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['post'], url_name='login')
    def login(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(email=email, password=password)
        
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({'detail':'Credencias invalidas'}, status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=False, methods=['get'], url_name='getme', permission_classes=[permissions.IsAuthenticated], authentication_classes=[SessionAuthentication])
    def getme(self, request):
        return Response({
                        'username': request.user.username,
                        'email': request.user.email
                        })