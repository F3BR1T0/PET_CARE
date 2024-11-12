from ..base_viewset import *
import requests
from django.conf import settings
from ...serializers import OwnerSaveWithMiranteSerializer, AddressSerializer

class MiranteViewSet(BaseAuthenticatedViewSet):    
    @action(detail=False, methods=['post'], url_path="create-with-mirante")
    def create_with_mirante(self, request):
        token = self.__login()
        data_mirante = self.__request_to_mirante(token)
        vipcep = self.__request_to_cep(data_mirante.get('cep'))
        address_data = {
            "cep": vipcep.get("cep", "").replace('-',''),
            "street": vipcep.get("logradouro", ""),
            "city": vipcep.get("localidade", ""),
            "state": vipcep.get("uf", ""),
            "country": "Brasil",
        }
        address_serializer = AddressSerializer(data=address_data)
        serializer = OwnerSaveWithMiranteSerializer(data=data_mirante)

        serializer.is_valid(raise_exception=True)
        address_serializer.is_valid(raise_exception=True)

        address_saved = address_serializer.save()

        if address_saved:
            saved = serializer.save(address=address_saved, account=self._get_user_authenticated())
            if saved:
                return Response(serializer.data,)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


    def __login(self):
        data = {
            "email":settings.JUNO_EMAIL,
            "password":settings.JUNO_PASSWORD
        }
        response = requests.post(url=settings.JUNO_LOGIN, json=data)
        if response.status_code == status.HTTP_200_OK:
            data = response.json()
            return data.get('token')
        else:
            return None

    def __request_to_mirante(self, token):
        data = {
            "user_email":"user@mirante.example"
        }
        url = settings.JUNO_FIND
        headers = {'Authorization':f'Bearer {token}'}

        response = requests.post(url, json=data, headers=headers)
        if response.status_code == status.HTTP_200_OK:
            return response.json().get('user')
        return response.json()
    
    def __request_to_cep(self, cep):
        url = f"https://viacep.com.br/ws/{cep}/json/"

        response = requests.get(url)
        return response.json()




    
