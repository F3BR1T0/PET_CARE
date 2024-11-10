from django.db import models
from .address import Address
from authentication.models import Account
from uuid import uuid4

def upload_image(instance, filename):
    return f'images/{instance.id}-{filename}'

class Owner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=upload_image)
    cpf = models.CharField(max_length=11)
    phone = models.CharField(max_length=11)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    occupation = models.CharField(max_length=255)
    account = models.OneToOneField(Account,on_delete=models.CASCADE, null=True)
    
    def delete(self):
        if self.address:
            self.address.delete()
        return super().delete(self)