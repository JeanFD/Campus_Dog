# Generated by Django 5.0.6 on 2024-08-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='descricao_completa',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
