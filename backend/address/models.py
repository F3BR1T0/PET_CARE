from django.db import models
from uuid import uuid4

class Address(models.Model):
    id_address = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
