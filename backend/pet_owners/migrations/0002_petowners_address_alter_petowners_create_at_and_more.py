# Generated by Django 5.1.1 on 2024-10-09 13:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('pet_owners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petowners',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='address.address'),
        ),
        migrations.AlterField(
            model_name='petowners',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='petowners',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]