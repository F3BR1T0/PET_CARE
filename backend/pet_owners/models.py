from django.db import models
from uuid import uuid4
# Create your models here.

class PetOwners(models.Model):
    id_pet_owners = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    foto = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=11)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)