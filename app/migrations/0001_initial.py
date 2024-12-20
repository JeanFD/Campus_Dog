# Generated by Django 5.0.6 on 2024-08-28 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('raca', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('vacinado', models.BooleanField(default=False)),
                ('descricao', models.TextField()),
                ('foto', models.ImageField(upload_to='fotos_animais/')),
            ],
        ),
    ]
