# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Inventario(models.Model):
	cantidad_pacas = models.IntegerField()
	cantidad_carretillos = models.IntegerField()
	cantidad_palas = models.IntegerField()
	cantidad_desparasitantes = models.IntegerField()
	cantidad_ordenadoras = models.IntegerField() 
	cantidad_estanon_miel = models.IntegerField()