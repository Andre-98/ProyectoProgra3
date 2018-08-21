from __future__ import unicode_literals

from __future__ import absolute_import

from django import forms

from apps.Animal.models import Animal


class AnimalForm(forms.ModelForm):

	class Meta:
		model = Animal

		fields = [
			'identificacion_numerica',
			'nombre',
			'sexo', 
			'fecha_nacimiento', 
			'edad',  
			'raza', 
			'foto', 
		]
		labels = {
			'identificacion_numerica': 'Identificacion Numerica',
			'nombre': 'Nombre',
			'sexo': 'Sexo', 
			'fecha_nacimiento': 'Fecha Nacimiento', 
			'edad': 'Edad',  
			'raza': 'Raza', 
			'foto': 'Foto',	
		}
		widgets = {
			'identificacion_numerica': forms.TextInput(attrs={'class': 'form-control'}),
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'sexo': forms.TextInput(attrs={'class': 'form-control'}), 
			'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control'}), 
			'edad': forms.TextInput(attrs={'class': 'form-control'}),  
			'raza': forms.TextInput(attrs={'class': 'form-control'}), 
			'foto': forms.TextInput(attrs={'class': 'form-control'}),	
		}