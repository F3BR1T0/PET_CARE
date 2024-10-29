from .base_viewset import *
from ..serializers import PetOwnerCreateUpdateSerializer, PetOwnerSerializer

class PetOwnerViewSet(mixins.CreateModelMixin, PetOwnerBaseViewSet, ResponseMixin):    
    def get_serializer_class(self):
        return PetOwnerCreateUpdateSerializer
    
    def create(self, request, *args, **kwargs):
        user = self.get_queryset()
        email = request.data['email']
        
        if user:
            return http.response('User already registered')
        if email != self.request.user.email:
            return http.response_bad_request_400('Email is not the same as your account')
        return super().create(request, *args, **kwargs)
    
    @action(detail=False, methods=['put'], url_name='update', url_path="update")
    def update_petowner(self, request):
        serializer = self.get_serializer(data=request.data, instance=self.get_queryset())
        account = self._get_account()
        
        petowner_updated = self.handle_serializer_errors(serializer)
        
        if petowner_updated:
            account.email = serializer.validated_data['email']
            account.save()
            return http.response_as_json(serializer.data, status.HTTP_202_ACCEPTED)
        
    @action(detail=False, methods=['get'])
    def get(self, request):
        petowner = self.get_queryset()
        if petowner is None:
                return http.response_bad_request_400('Not registered.')
        return http.response_as_json(PetOwnerSerializer(petowner).data)
           
    @action(detail=False, methods=['delete'], url_name='delete')
    def delete(self, request):
        user = self.get_queryset()
        if user is None:
            return http.response_bad_request_400("Not registered.")    
        
        account = self._get_account()
        if account is None:
            return http.response_bad_request_400("Account not found.")
        
        try:
            user.delete()
            account.delete()
            logout(request)
            return http.response("User deleted successfuly", status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return http.response_bad_request_400(str(e))