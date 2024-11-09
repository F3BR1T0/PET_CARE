from .base_owner_viewset import BaseOwnerAuthenticatedViewSet, mixins, Response, status, action
from ...serializers import OwnerSaveSerializer, OwnerSerializer, AddressSerializer

class OwnerViewSet(BaseOwnerAuthenticatedViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    def get_serializer_class(self):
        actions = {
            "me": OwnerSerializer,
            "address": AddressSerializer,
            "address_update": AddressSerializer,
        }
        return actions.get(self.action, OwnerSaveSerializer)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
    
        serializer.is_valid(raise_exception=True)    
        
        owner_saved = serializer.save(account = self._get_user())
        
        if owner_saved:
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        return Response(self.get_serializer(self.get_queryset().first()).data)
    
    @action(detail=False, methods=['post'], url_name="create address", url_path="address")
    def address(self, request):
        owner = self.get_queryset().first()
        if owner.address:
            return Response('Address already exists.')
        
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        address_saved = serializer.save()
        
        if address_saved:
            owner.address = address_saved
            owner.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['put'], url_name="update address", url_path="address-update")
    def address_update(self, request):
        serializer = self.get_serializer(data=request.data, instance = self.get_queryset().first().address)
        serializer.is_valid(raise_exception=True)
        
        address_saved = serializer.save()
        
        if address_saved:
            return Response(serializer.data, status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
        