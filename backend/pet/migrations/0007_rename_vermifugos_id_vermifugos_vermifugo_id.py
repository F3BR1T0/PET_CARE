# Generated by Django 5.1.2 on 2024-10-24 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0006_alter_cirurgia_historico_medico_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vermifugos',
            old_name='vermifugos_id',
            new_name='vermifugo_id',
        ),
    ]
