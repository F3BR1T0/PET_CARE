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
        
class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacinas
        exclude = ['vacina_id']
        
class VacinasAdministradasSerializer(serializers.ModelSerializer):
    vacina = VacinaSerializer()
    class Meta:
        model = models.VacinasAdministradas
        fields = '__all__'
class VacinaAdministradasSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VacinasAdministradas
        fields = '__all__'
class VacinaAdministradasUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VacinasAdministradas
        exclude = ('historico_medico',)
        
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

        
class HistoricoMedicoSerializer(serializers.ModelSerializer):
    pet = PetSerializer(read_only=True)
    vacinas_administradas = VacinasAdministradasSerializer(many=True, read_only=True)
    class Meta:
        model = models.HistoricoMedico
        fields = '__all__'
        
    