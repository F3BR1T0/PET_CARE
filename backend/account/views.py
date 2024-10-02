from django.contrib.auth import logout
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from account.api.serializers import AccountRegisterSerializer
from rest_framework import permissions, status


class AccountRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = AccountRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class AccountLogout(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)