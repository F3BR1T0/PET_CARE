from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext_lazy as _


class HttpResponseUtils:
    def response(msg, statuscode=status.HTTP_200_OK):
        return Response({'detail': _(msg)}, status=statuscode)
    
    def response_as_json(json, statuscode=status.HTTP_200_OK):
        return Response(json, status=statuscode)
    
    def response_empy(statuscode=status.HTTP_200_OK):
        return Response(status=statuscode)
    
    def response_bad_request_400(msg):
        return Response({'error': msg }, status.HTTP_400_BAD_REQUEST)