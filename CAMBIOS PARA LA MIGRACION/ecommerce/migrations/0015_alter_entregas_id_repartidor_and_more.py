# Generated by Django 5.0.6 on 2024-06-21 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0014_agenda_entregas_pedido_agenda_id_pedido'),
        ('repartidor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregas',
            name='id_repartidor',
            field=models.ForeignKey(db_column='id_repatidor', on_delete=django.db.models.deletion.CASCADE, to='repartidor.repartidor'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='id_repartidor',
            field=models.ForeignKey(blank=True, db_column='id_repatidor', null=True, on_delete=django.db.models.deletion.CASCADE, to='repartidor.repartidor'),
        ),
    ]
