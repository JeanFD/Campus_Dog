# Generated by Django 5.1.2 on 2024-11-16 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_desenvolvedores_rename_raça_raca_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Desenvolvedores',
            new_name='Desenvolvedor',
        ),
        migrations.AlterModelOptions(
            name='desenvolvedor',
            options={'verbose_name': 'Desenvolvedor', 'verbose_name_plural': 'Desenvolvedores'},
        ),
    ]
