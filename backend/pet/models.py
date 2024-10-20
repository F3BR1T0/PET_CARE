from django.db import models
from pet_owners.models import PetOwners
from uuid import uuid4

class Pet(models.Model):
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('F', 'Femea')    
    ]
    
    pet_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    pet_owner = models.ForeignKey(PetOwners, on_delete=models.CASCADE, null=False)
    nome = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    raca = models.CharField(max_length=255)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
class HistoricoMedico(models.Model):
    historico_medico_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Vacinas(models.Model):
    vacina_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Vermifugos(models.Model):
    vermifugos_id = models.URLField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Doecas(models.Model):
    doencas_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    sintomas = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
class VacinasAdministradas(models.Model):
    vacinas_administradas_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    historico_medico = models.ForeignKey(HistoricoMedico, on_delete=models.CASCADE)
    vacina = models.ForeignKey(Vacinas, on_delete=models.CASCADE,)
    data_aplicacao = models.DateTimeField()
    data_reforco = models.DateTimeField(null=True, blank=True)

class VermifugosAdministrados(models.Model):
    vermifugos_administrados_id = models.URLField(primary_key=True, default=uuid4, editable=False)
    historico_medico = models.ForeignKey(HistoricoMedico, on_delete=models.CASCADE)
    vermifugo = models.ForeignKey(Vermifugos, on_delete=models.CASCADE,)
    data_aplicacao = models.DateTimeField()
    data_reforco = models.DateTimeField(null=True, blank=True)

class DoencasDocumentadas(models.Model):
    STATUS_CHOICES = [
        ('em_tratamento', 'Em tratamento'),
        ('curado', 'Curado'),
        ('em_monitoramento', 'Em monitoramento'),
        ('sem_diagnostico', 'Sem diagnóstico'),
    ]
    
    doencas_documentadas_id = models.URLField(primary_key=True, default=uuid4, editable=False)
    historico_medico = models.ForeignKey(HistoricoMedico, on_delete=models.CASCADE)
    doenca = models.ForeignKey(Doecas, on_delete=models.CASCADE,)
    data_diagnostico = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    
class Cirurgia(models.Model):
    cirurgia_id = models.URLField(primary_key=True, default=uuid4, editable=False)
    historico_medico = models.ForeignKey(HistoricoMedico, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    data = models.DateTimeField()
    descricao = models.TextField()
    resultado = models.CharField(max_length=100, choices=[
        ('sucesso', 'Sucesso'),
        ('falha', 'Falha'),
        ('em_recuperacao', 'Em recuperação'),
        ('sem_informacao', 'Sem informação'),
    ])
