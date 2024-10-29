from .base_viewset import *
from ..serializers import PetOwnerEmailSerializer
from ..permissions import HasShareJunoApiKey
from ..authentications import CustomJunoAuthentication

class PetOwnerExtraViewSet(viewsets.GenericViewSet):
    permission_classes = [HasShareJunoApiKey]
    authentication_classes = [CustomJunoAuthentication]
    
    def __get_petowner_by_email(self, _email):
        return models.PetOwner.objects.filter(email=_email).first()
    
    def get_serializer_class(self):
        return PetOwnerEmailSerializer
    
    @action(detail=False, methods=['post'])
    def findbyemail(self, request):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            petowner = self.__get_petowner_by_email(serializer.data.get('email'))
            if petowner is None:
                return http.response_bad_request_400("Not found.")
            return http.response_as_json({
                'email': petowner.email,
                'name': petowner.nome,
                'city': petowner.endereco.cidade,
                'occupation':'not implemented'
            })
        return http.response_as_json(serializer.errors, status.HTTP_400_BAD_REQUEST)