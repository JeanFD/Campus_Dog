# Generated by Django 5.1.2 on 2025-01-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_animal_criado_por'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusuario',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
