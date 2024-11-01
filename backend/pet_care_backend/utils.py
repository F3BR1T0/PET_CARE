from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.utils.translation import gettext_lazy as _


class HttpResponseUtils:
    def response(msg, statuscode=status.HTTP_200_OK):
        return Response({'detail': _(msg)}, status=statuscode)
    
    def response_as_json(json, statuscode=status.HTTP_200_OK):
        return Response(json, status=statuscode)
    
    def response_empty(statuscode=status.HTTP_200_OK):
        return Response(status=statuscode)
    
    def response_bad_request_400(msg):
        return Response({'error': msg }, status.HTTP_400_BAD_REQUEST)
    
class ResponseMixin:
    def handle_serializer_errors(self, serializer):
        if serializer.is_valid(raise_exception=True):
            try:
                return serializer.save()
            except Exception as e:
                return HttpResponseUtils.response_bad_request_400(str(e))
        return HttpResponseUtils.response_as_json(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
class SerializerUtils:
    class BaseModelSerializer(serializers.ModelSerializer):
        class Meta:
            fields = '__all__'
    
    class BaseModelExcludeSerializer(serializers.ModelSerializer):
        class Meta:
            exclude = ['']
        