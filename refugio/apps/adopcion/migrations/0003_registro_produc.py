# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-19 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0002_solicitud'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_produc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_produccion', models.CharField(max_length=10)),
                ('fecha_produccion', models.DateField()),
                ('cantidad_producida', models.IntegerField()),
                ('tipo', models.CharField(choices=[('Botellas', 'Botellas'), ('Litros', 'Litros'), ('Galones', 'Galones')], default='Botellas', max_length=10)),
            ],
        ),
    ]
