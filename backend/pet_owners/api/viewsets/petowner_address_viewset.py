from .base_viewset import *
from ..serializers import AddressSerializer

class PetOwnerAddressViewSet(PetOwnerBaseViewSet, ResponseMixin):    
    def get_serializer_class(self):
        return AddressSerializer
    
        
    @action(detail=False, methods=['post'], url_name="create-address", url_path="create")
    def create_address(self, request):
        serializer = self.get_serializer(data=request.data)
        petowner = self.get_queryset()
        
        if petowner is None:
            return http.response_bad_request_400("Not registered.")
        
        if petowner.endereco is not None:
            return http.response_bad_request_400("Already have a address.")
        
        address_created = self.handle_serializer_errors(serializer)
        
        if address_created:
            petowner.endereco = address_created
            petowner.save()
            return http.response_as_json(serializer.data, status.HTTP_201_CREATED)
   
    @action(detail=False, methods=['put'], url_name="update-address", url_path="update")
    def update_address(self, request):
        petowner = self.get_queryset()
        if petowner.endereco is None:
            return http.response_bad_request_400("Petowner does not have a address.")
        
        serializer = self.get_serializer(data=request.data, instance=petowner.endereco)
        
        address_updated = self.handle_serializer_errors(serializer)
        
        if address_updated:
            return http.response_as_json(serializer.data, status.HTTP_202_ACCEPTED)