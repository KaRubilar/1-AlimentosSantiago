# Generated by Django 5.0.6 on 2024-06-11 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='foto_categoria',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='plato',
            name='foto_plato',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
