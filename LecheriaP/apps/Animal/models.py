# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import

from django.db import models

#from apps.Produccion.models import Registro_Produccion

# Create your models here.

class Animal(models.Model):
	
	identificacion_numerica = models.IntegerField()
	nombre = models.CharField(max_length=50)
	sexo = models.CharField(max_length=10)
	fecha_nacimiento = models.DateField()
	edad = models.IntegerField() 
	raza = models.CharField(max_length=10)
	foto = models.CharField(max_length=10)
	Ternera = 'Ternera'
	Ternero = 'Ternero'
	Novilla = 'Novilla'
	Novillo = 'Novillo'
	Vaca = 'Vaca'
	Toro = 'Toro'
	Etapa = (
		(Ternera, 'Ternera'),
		(Ternero, 'Ternero'),
		(Novilla, 'Novilla'),
		(Novillo, 'Novillo'),
		(Vaca, 'Vaca'),
		(Toro, 'Toro'),
	)
	etapa = models.CharField(
		max_length = 10,
		choices = Etapa, 
		default = Vaca,
	)
	def is_upperclass(self):
		return self.etapa in (self.Ternera, self.Ternero, self.Novilla, self.Novillo, self.Vaca, self.Toro)
	
	Prenada = 'Preñada'
	Produciendo = 'Produciendo'
	No_Produciendo = 'No Produciendo'
	Estado = (
		(Prenada, 'Preñada'),
		(Produciendo, 'Produciendo'),
		(No_Produciendo, 'No Produciendo'),
	)
	estado = models.CharField(
		max_length = 20,
		choices = Estado, 
		default = No_Produciendo,
	)
	def is_upperclass(self):
		return self.estado in (self.Prenada, self.Produciendo, self.No_Produciendo)		
	#fecha_inicio_parto = models.DateField() 
	#fecha_aproximada_parto = models.DateField()
	#Produccion = models.OneToOneField(Registro_Produccion, null=True, blank=True, on_delete=models.CASCADE)
	cantidad_partos = models.IntegerField()

