# Generated by Django 5.1.2 on 2024-10-21 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0004_remove_doecas_create_at_remove_doecas_update_at_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doecas',
            new_name='Doencas',
        ),
    ]
