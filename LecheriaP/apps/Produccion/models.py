# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import

from django.db import models

from apps.Animal.models import Animal

# Create your models here.


class Registro_Produccion(models.Model):
	Individual = 'Individual'
	Grupal = 'Grupal'
	Produccion_Diaria = (
		(Individual, 'Individual'),
		(Grupal, 'Grupal'),
	)
	produccion_diaria = models.CharField(
		max_length = 20,
		choices = Produccion_Diaria, 
		default = Individual,
	)
	def is_upperclass(self):
		return self.produccion_diaria in (self.Individual, self.Grupal)
	#animal = models.ForeignKey(Animal, null=True, blank=True, on_delete=models.CASCADE)
	Animales = models.ManyToManyField(Animal)
	fecha_produccion = models.DateField()
	cantidad_producida = models.IntegerField()
	Botellas = 'Botellas'
	Litros = 'Litros'
	Galones = 'Galones'
	Unidad_De_Medida = (
		(Botellas, 'Botellas'),
		(Litros, 'Litros'),
		(Galones, 'Galones'),
	)
	unidad_de_medida = models.CharField(
		max_length = 10,
		choices = Unidad_De_Medida, 
		default = Botellas,
	)
	
	def is_upperclass(self):
		return self.unidad_de_medida in (self.Botellas, self.Litros, self.Galones)



