from django.db import models
from uuid import uuid4

class MedicalHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    obs = models.TextField()
    