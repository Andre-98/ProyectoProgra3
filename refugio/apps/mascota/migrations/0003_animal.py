# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-19 23:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0003_registro_produc'),
        ('mascota', '0002_auto_20180806_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Vaca', 'Vaca'), ('Toro', 'Toro')], default='Vaca', max_length=10)),
                ('identificacion_numerica', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('fecha_nacimiento', models.DateField()),
                ('edad', models.IntegerField()),
                ('raza', models.CharField(max_length=10)),
                ('foto', models.CharField(max_length=10)),
                ('etapa', models.CharField(max_length=50)),
                ('estado_vaca', models.CharField(max_length=10)),
                ('cantidad_partos', models.IntegerField()),
                ('registro_produc', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adopcion.Registro_produc')),
            ],
        ),
    ]