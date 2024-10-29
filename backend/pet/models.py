from django.db import models
from pet_owners.models import PetOwner
from uuid import uuid4

class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    
    class Meta:
        abstract = True

class HistoricoMedico(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    observacoes = models.TextField(null=True)

class Pet(models.Model):
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('F', 'Femea')    
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    dono = models.ForeignKey(PetOwner, on_delete=models.CASCADE, null=False)
    nome = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    raca = models.CharField(max_length=255)
    peso = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    historico_medico = models.OneToOneField(HistoricoMedico, on_delete=models.CASCADE, default=None)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Vacina(Base):
    pass

class Vermifugo(Base):
    pass

class Doenca(Base):
    descricao = models.TextField(null=True)
    sintomas = models.TextField()

class MedicamentoAdministrado(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    historico_medico = models.ForeignKey(HistoricoMedico, on_delete=models.CASCADE)
    vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE, null=True, blank=True)
    vermifugo = models.ForeignKey(Vermifugo, on_delete=models.CASCADE, null=True, blank=True)
    observacao = models.TextField(null=True)
    data_aplicacao = models.DateTimeField()
    data_reforco = models.DateTimeField(null=True, blank=True)

class DoencaDocumentada(models.Model):
    STATUS_CHOICES = [
        ('em_tratamento', 'Em tratamento'),
        ('curado', 'Curado'),
        ('em_monitoramento', 'Em monitoramento'),
        ('sem_diagnostico', 'Sem diagnóstico'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    historico_medico = models.ForeignKey(HistoricoMedico, on_delete=models.CASCADE, related_name='doencas_administradas')
    doenca = models.ForeignKey(Doenca, on_delete=models.CASCADE)
    observacao = models.TextField(null=True)
    data_diagnostico = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    
class Cirurgia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    historico_medico = models.ForeignKey(HistoricoMedico, on_delete=models.CASCADE, related_name='cirurgias_administradas')
    nome = models.CharField(max_length=100)
    data = models.DateTimeField()
    descricao = models.TextField()
    resultado = models.CharField(max_length=100, choices=[
        ('sucesso', 'Sucesso'),
        ('falha', 'Falha'),
        ('em_recuperacao', 'Em recuperação'),
        ('sem_informacao', 'Sem informação'),
    ])
