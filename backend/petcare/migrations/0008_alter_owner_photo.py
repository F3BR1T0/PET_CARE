# Generated by Django 5.1.2 on 2024-11-10 17:14

import petcare.models.owner
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petcare', '0007_alter_owner_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='photo',
            field=models.ImageField(upload_to=petcare.models.owner.upload_image),
        ),
    ]