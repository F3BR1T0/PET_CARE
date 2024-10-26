from rest_framework import serializers
from pet import models

# Base para modelos com serialização completa
class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

# Base para serializers que exigem exclusão de campos
class BaseExcludeOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['pet_owner']

# Serializers para modelos específicos

class PetSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Pet

class PetSaveSerializer(BaseExcludeOwnerSerializer):
    class Meta(BaseExcludeOwnerSerializer.Meta):
        model = models.Pet

class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacinas
        exclude = ['vacina_id']

class VacinasAdministradasSerializer(BaseSerializer):
    vacina = VacinaSerializer()
    class Meta(BaseSerializer.Meta):
        model = models.VacinasAdministradas

class VacinaAdministradasSaveSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.VacinasAdministradas

class VacinaAdministradasUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VacinasAdministradas
        exclude = ('historico_medico',)

class VermifugoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vermifugos
        exclude = ['vermifugo_id']

class VermifugosAdministradosSerializer(BaseSerializer):
    vermifugo = VermifugoSerializer()
    class Meta(BaseSerializer.Meta):
        model = models.VermifugosAdministrados

class VermifugosAdministradosSaveSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.VermifugosAdministrados

class VermifugosAdministradosUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VermifugosAdministrados
        exclude = ['historico_medico']

class DoencasDocumentadasSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.DoencasDocumentadas

class CirurgiaSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Cirurgia

class HistoricoMedicoSerializer(BaseSerializer):
    pet = PetSerializer(read_only=True)
    vacinas_administradas = VacinasAdministradasSerializer(many=True, read_only=True)
    class Meta(BaseSerializer.Meta):
        model = models.HistoricoMedico
