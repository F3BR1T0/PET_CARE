# Generated by Django 5.1.2 on 2024-10-29 02:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicomedico',
            name='pet',
        ),
        migrations.AddField(
            model_name='pet',
            name='historico_medico',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='pet.historicomedico'),
        ),
    ]