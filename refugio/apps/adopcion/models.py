# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import

from django.db import models

from apps.mascota.models import Animal

# Create your models here.


class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=70)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=12)
	email = models.EmailField()
	domicilio = models.TextField()



	def __unicode__(self):
		return '{} {}'.format(self.nombre, self.apellidos)


class Solicitud(models.Model):
	persona = models.ForeignKey(Persona, null=True, blank=True)
	numero_mascotas = models.IntegerField()
	razones = models.TextField()

class Registro_produc(models.Model):
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
	animal = models.OneToOneField(Animal, null=True, blank=True, on_delete=models.CASCADE)
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

