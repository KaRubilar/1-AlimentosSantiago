# Generated by Django 5.0.6 on 2024-06-21 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repartidor',
            fields=[
                ('id_repartidor', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=12)),
                ('nombre_repartidor', models.CharField(max_length=100)),
                ('numero_telf', models.CharField(max_length=15)),
            ],
        ),
    ]
