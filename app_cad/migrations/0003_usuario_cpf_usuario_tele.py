# Generated by Django 5.1.7 on 2025-04-03 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cpf',
            field=models.TextField(default='000.000.000-00'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tele',
            field=models.TextField(default=''),
        ),
    ]
