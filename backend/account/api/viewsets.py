from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from account.api.serializers import AccountRegisterSerializer
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework import permissions, status

class AccountRegisterViewSet(viewsets.ViewSet):
    serializer_class = AccountRegisterSerializer

    def register(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AccountLogoutViewSet(viewsets.ViewSet):
    serializer_class = None

    def logout(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
