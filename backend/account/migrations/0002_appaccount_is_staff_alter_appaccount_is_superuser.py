# Generated by Django 5.1.1 on 2024-10-02 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appaccount',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appaccount',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
