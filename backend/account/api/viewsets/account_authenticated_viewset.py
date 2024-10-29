from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth import logout
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions

from ..serializers import AccountUpdateSerializer, AccountChangePasswordSerializer
from pet_care_backend.utils import HttpResponseUtils as http
from pet_care_backend.utils import ResponseMixin

class AccountAuthenticatedViewSet(viewsets.GenericViewSet, ResponseMixin):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    
    def get_serializer_class(self):
        action_serializers = {
            "change_password": AccountChangePasswordSerializer
        }
        return action_serializers.get(self.action, AccountUpdateSerializer)
    
    @action(detail=False, methods=['get'], url_name="get")
    def get(self,request):
        return http.response_as_json({
            'username': request.user.username,
            'email': request.user.email
        })
    
    @action(detail=False, methods=['put'], url_path="update", url_name="update")
    def update_account(self, request):
        serializer = self.get_serializer(instance=request.user, data=request.data)
        saved_user = self.handle_serializer_errors(serializer)
        if saved_user:
            return http.response_as_json(serializer.data, status.HTTP_202_ACCEPTED)
    
    @action(detail=False, methods=['put'], url_path="change-password", url_name="change-password")
    def change_password(self, request):
        serializer = self.get_serializer(data=request.data, instance=request.user)
        saved_user = self.handle_serializer_errors(serializer)
        if saved_user:
            logout(request)
            return http.response('Password changed successfully', status.HTTP_202_ACCEPTED)
    
    @action(detail=False, methods=['post'], url_path="logout")
    def logout(self, request):
        try:
            logout(request)
            return http.response('Logout completed successfully',status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return http.response_bad_request_400(str(e))