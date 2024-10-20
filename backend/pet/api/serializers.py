from rest_framework import serializers
from pet import models

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pet
        fields = '__all__'

class PetSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pet
        exclude = ['pet_owner']
        
class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HistoricoMedico
        fields = '__all__'
        
class VacinasAdministradasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VacinasAdministradas
        fields = '__all__'
        
class VermifugosAdministrados(serializers.ModelSerializer):
    class Meta:
        model = models.VermifugosAdministrados
        fields = '__all__'

class DoencasDocumentadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DoencasDocumentadas
        fields = '__all__'

class CirurgiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cirurgia
        fields = '__all__'
        
    