# Generated by Django 5.1.3 on 2024-11-25 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.CharField(default='cuid', max_length=36, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=50)),
                ('data_nascimento', models.DateField()),
                ('foto', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
